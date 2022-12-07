# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import chat_pb2 as chat__pb2


class ChattingStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ConnectServer = channel.unary_unary(
                '/Chatting/ConnectServer',
                request_serializer=chat__pb2.ConnectServerReqeust.SerializeToString,
                response_deserializer=chat__pb2.ConnectServerResponse.FromString,
                )
        self.ListenChat = channel.unary_stream(
                '/Chatting/ListenChat',
                request_serializer=chat__pb2.ListenRequest.SerializeToString,
                response_deserializer=chat__pb2.ChatResponse.FromString,
                )
        self.SendChat = channel.unary_unary(
                '/Chatting/SendChat',
                request_serializer=chat__pb2.ChatRequest.SerializeToString,
                response_deserializer=chat__pb2.Empty.FromString,
                )


class ChattingServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ConnectServer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListenChat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendChat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChattingServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ConnectServer': grpc.unary_unary_rpc_method_handler(
                    servicer.ConnectServer,
                    request_deserializer=chat__pb2.ConnectServerReqeust.FromString,
                    response_serializer=chat__pb2.ConnectServerResponse.SerializeToString,
            ),
            'ListenChat': grpc.unary_stream_rpc_method_handler(
                    servicer.ListenChat,
                    request_deserializer=chat__pb2.ListenRequest.FromString,
                    response_serializer=chat__pb2.ChatResponse.SerializeToString,
            ),
            'SendChat': grpc.unary_unary_rpc_method_handler(
                    servicer.SendChat,
                    request_deserializer=chat__pb2.ChatRequest.FromString,
                    response_serializer=chat__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Chatting', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Chatting(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ConnectServer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Chatting/ConnectServer',
            chat__pb2.ConnectServerReqeust.SerializeToString,
            chat__pb2.ConnectServerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListenChat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Chatting/ListenChat',
            chat__pb2.ListenRequest.SerializeToString,
            chat__pb2.ChatResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendChat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Chatting/SendChat',
            chat__pb2.ChatRequest.SerializeToString,
            chat__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
