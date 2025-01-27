import subprocess
import unittest
from typing import Any, List

import grpc

from indexify.function_executor.proto.configuration import GRPC_CHANNEL_OPTIONS
from indexify.function_executor.proto.function_executor_pb2 import (
    FunctionOutput,
    RunTaskRequest,
    RunTaskResponse,
    SerializedObject,
)
from indexify.function_executor.proto.function_executor_pb2_grpc import (
    FunctionExecutorStub,
)
from indexify.functions_sdk.object_serializer import CloudPickleSerializer


class FunctionExecutorServerTestCase(unittest.TestCase):
    FUNCTION_EXECUTOR_SERVER_ADDRESS = "localhost:50000"
    _functionExecutorServerProc: subprocess.Popen = None

    @classmethod
    def setUpClass(cls):
        # We setup one Function Executor server for all the tests running in this class.
        # If an exception is raised during a setUpClass then the tests in the class are
        # not run and the tearDownClass is not run.
        cls._functionExecutorServerProc = subprocess.Popen(
            [
                "indexify-cli",
                "function-executor",
                "--dev",
                "--function-executor-server-address",
                cls.FUNCTION_EXECUTOR_SERVER_ADDRESS,
            ]
        )

    @classmethod
    def tearDownClass(cls):
        if cls._functionExecutorServerProc is not None:
            cls._functionExecutorServerProc.kill()
            cls._functionExecutorServerProc.wait()

    def _rpc_channel(self) -> grpc.Channel:
        channel: grpc.Channel = grpc.insecure_channel(
            self.FUNCTION_EXECUTOR_SERVER_ADDRESS,
            options=GRPC_CHANNEL_OPTIONS,
        )
        try:
            SERVER_STARTUP_TIMEOUT_SEC = 5
            # This is not asyncio.Future but grpc.Future. It has a different interface.
            grpc.channel_ready_future(channel).result(
                timeout=SERVER_STARTUP_TIMEOUT_SEC
            )
            return channel
        except Exception as e:
            channel.close()
            self.fail(
                f"Failed to connect to the gRPC server within {SERVER_STARTUP_TIMEOUT_SEC} seconds: {e}"
            )


def run_task(stub: FunctionExecutorStub, input: Any) -> RunTaskResponse:
    return stub.run_task(
        RunTaskRequest(
            graph_invocation_id="123",
            task_id="test-task",
            function_input=SerializedObject(
                bytes=CloudPickleSerializer.serialize(input),
                content_type=CloudPickleSerializer.content_type,
            ),
        )
    )


def deserialized_function_output(
    test_case: unittest.TestCase, function_output: FunctionOutput
) -> List[Any]:
    outputs: List[Any] = []
    for output in function_output.outputs:
        test_case.assertEqual(output.content_type, CloudPickleSerializer.content_type)
        outputs.append(CloudPickleSerializer.deserialize(output.bytes))
    return outputs
