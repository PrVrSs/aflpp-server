import grpc

from aflpp_server.aflpp import AFLPP
from aflpp_server.protoc.v1.aflpp_pb2 import StartRequest, StartResponse, StopRequest, StopResponse
from aflpp_server.protoc.v1.aflpp_pb2_grpc import AFLPPServicer as _AFLPPServicer


class AFLPPServicer(_AFLPPServicer):
    def __init__(self, aflpp: AFLPP):
        self._aflpp = aflpp

    async def start(self, request: StartRequest, context: grpc.aio.ServicerContext) -> StartResponse:
        return StartResponse(
            success=await self._aflpp.start(
                source=request.binary,
                aflpp_args=request.aflpp_args,
                binary_args=request.binary_args,
                seeds=request.seeds,
            )
        )

    async def stop(self, request: StopRequest, context: grpc.aio.ServicerContext) -> StopResponse:
        await self._aflpp.stop()
        return StopResponse(success=True)