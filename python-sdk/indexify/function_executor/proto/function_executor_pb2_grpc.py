# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import warnings

import grpc

from indexify.function_executor.proto import (
    function_executor_pb2 as indexify_dot_function__executor_dot_proto_dot_function__executor__pb2,
)

GRPC_GENERATED_VERSION = "1.68.1"
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower

    _version_not_supported = first_version_is_lower(
        GRPC_VERSION, GRPC_GENERATED_VERSION
    )
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f"The grpc package installed is at version {GRPC_VERSION},"
        + f" but the generated code in indexify/function_executor/proto/function_executor_pb2_grpc.py depends on"
        + f" grpcio>={GRPC_GENERATED_VERSION}."
        + f" Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}"
        + f" or downgrade your generated code using grpcio-tools<={GRPC_VERSION}."
    )


class FunctionExecutorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.initialize = channel.unary_unary(
            "/function_executor_service.FunctionExecutor/initialize",
            request_serializer=indexify_dot_function__executor_dot_proto_dot_function__executor__pb2.InitializeRequest.SerializeToString,
            response_deserializer=indexify_dot_function__executor_dot_proto_dot_function__executor__pb2.InitializeResponse.FromString,
            _registered_method=True,
        )
        self.initialize_invocation_state_server = channel.stream_stream(
            "/function_executor_service.FunctionExecutor/initialize_invocation_state_server",
            request_serializer=indexify_dot_function__executor_dot_proto_dot_function__executor__pb2.InvocationStateResponse.SerializeToString,
            response_deserializer=indexify_dot_function__executor_dot_proto_dot_function__executor__pb2.InvocationStateRequest.FromString,
            _registered_method=True,
        )
        self.run_task = channel.unary_unary(
            "/function_executor_service.FunctionExecutor/run_task",
            request_serializer=indexify_dot_function__executor_dot_proto_dot_function__executor__pb2.RunTaskRequest.SerializeToString,
            response_deserializer=indexify_dot_function__executor_dot_proto_dot_function__executor__pb2.RunTaskResponse.FromString,
            _registered_method=True,
        )


class FunctionExecutorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def initialize(self, request, context):
        """Initializes the Function Executor to run tasks
        for a particular function. This method is called only
        once per Function Executor as it can only run a single function.
        It should be called before calling RunTask for the function.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def initialize_invocation_state_server(self, request_iterator, context):
        """Initializes a server that sends requests to the client to perform actions on
        a task's graph invocation state. This method is called only once per Function Executor
        It should be called before calling RunTask for the function.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def run_task(self, request, context):
        """Executes the task defined in the request.
        Multiple tasks can be running in parallel.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_FunctionExecutorServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "initialize": grpc.unary_unary_rpc_method_handler(
            servicer.initialize,
            request_deserializer=indexify_dot_function__executor_dot_proto_dot_function__executor__pb2.InitializeRequest.FromString,
            response_serializer=indexify_dot_function__executor_dot_proto_dot_function__executor__pb2.InitializeResponse.SerializeToString,
        ),
        "initialize_invocation_state_server": grpc.stream_stream_rpc_method_handler(
            servicer.initialize_invocation_state_server,
            request_deserializer=indexify_dot_function__executor_dot_proto_dot_function__executor__pb2.InvocationStateResponse.FromString,
            response_serializer=indexify_dot_function__executor_dot_proto_dot_function__executor__pb2.InvocationStateRequest.SerializeToString,
        ),
        "run_task": grpc.unary_unary_rpc_method_handler(
            servicer.run_task,
            request_deserializer=indexify_dot_function__executor_dot_proto_dot_function__executor__pb2.RunTaskRequest.FromString,
            response_serializer=indexify_dot_function__executor_dot_proto_dot_function__executor__pb2.RunTaskResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "function_executor_service.FunctionExecutor", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers(
        "function_executor_service.FunctionExecutor", rpc_method_handlers
    )


# This class is part of an EXPERIMENTAL API.
class FunctionExecutor(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def initialize(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/function_executor_service.FunctionExecutor/initialize",
            indexify_dot_function__executor_dot_proto_dot_function__executor__pb2.InitializeRequest.SerializeToString,
            indexify_dot_function__executor_dot_proto_dot_function__executor__pb2.InitializeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def initialize_invocation_state_server(
        request_iterator,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            "/function_executor_service.FunctionExecutor/initialize_invocation_state_server",
            indexify_dot_function__executor_dot_proto_dot_function__executor__pb2.InvocationStateResponse.SerializeToString,
            indexify_dot_function__executor_dot_proto_dot_function__executor__pb2.InvocationStateRequest.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def run_task(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/function_executor_service.FunctionExecutor/run_task",
            indexify_dot_function__executor_dot_proto_dot_function__executor__pb2.RunTaskRequest.SerializeToString,
            indexify_dot_function__executor_dot_proto_dot_function__executor__pb2.RunTaskResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )
