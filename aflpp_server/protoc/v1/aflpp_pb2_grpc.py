# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protoc.v1 import aflpp_pb2 as protoc_dot_v1_dot_aflpp__pb2


class AFLPPStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.start = channel.unary_unary(
                '/aflpp.v1.AFLPP/start',
                request_serializer=protoc_dot_v1_dot_aflpp__pb2.StartRequest.SerializeToString,
                response_deserializer=protoc_dot_v1_dot_aflpp__pb2.StartResponse.FromString,
                )
        self.stop = channel.unary_unary(
                '/aflpp.v1.AFLPP/stop',
                request_serializer=protoc_dot_v1_dot_aflpp__pb2.StopRequest.SerializeToString,
                response_deserializer=protoc_dot_v1_dot_aflpp__pb2.StopResponse.FromString,
                )


class AFLPPServicer(object):
    """Missing associated documentation comment in .proto file."""

    def start(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stop(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AFLPPServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'start': grpc.unary_unary_rpc_method_handler(
                    servicer.start,
                    request_deserializer=protoc_dot_v1_dot_aflpp__pb2.StartRequest.FromString,
                    response_serializer=protoc_dot_v1_dot_aflpp__pb2.StartResponse.SerializeToString,
            ),
            'stop': grpc.unary_unary_rpc_method_handler(
                    servicer.stop,
                    request_deserializer=protoc_dot_v1_dot_aflpp__pb2.StopRequest.FromString,
                    response_serializer=protoc_dot_v1_dot_aflpp__pb2.StopResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'aflpp.v1.AFLPP', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AFLPP(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def start(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aflpp.v1.AFLPP/start',
            protoc_dot_v1_dot_aflpp__pb2.StartRequest.SerializeToString,
            protoc_dot_v1_dot_aflpp__pb2.StartResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def stop(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aflpp.v1.AFLPP/stop',
            protoc_dot_v1_dot_aflpp__pb2.StopRequest.SerializeToString,
            protoc_dot_v1_dot_aflpp__pb2.StopResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)