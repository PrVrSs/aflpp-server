import asyncio

import grpc
import janus

from aflpp_server.aflpp import AFLPP
from aflpp_server.helper import async_run, cleanup_coroutines
from aflpp_server.logger import logger
from aflpp_server.process import AFLProcess
from aflpp_server.protoc.aflpp_pb2 import StartResponse, StartRequest, StopResponse, StopRequest
from aflpp_server.protoc.aflpp_pb2_grpc import AFLPPServicer as _AFLPPServicer
from aflpp_server.protoc.aflpp_pb2_grpc import add_AFLPPServicer_to_server
from aflpp_server.settings import settings
from aflpp_server.workspace import Workspace


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


class AFLPPServer:
    def __init__(self, aflpp: AFLPP):
        self._aflpp = aflpp
        self._server = grpc.aio.server()
        self._aflpp_servicer = AFLPPServicer(aflpp)

        add_AFLPPServicer_to_server(self._aflpp_servicer, self._server)
        self._server.add_insecure_port(f'{settings.host}:{settings.port}')

        cleanup_coroutines.append(self.shutdown())

    async def run(self) -> None:
        logger.info(f'Starting server on {settings.host}:{settings.port}')

        await self._server.start()
        await self._server.wait_for_termination()

    async def shutdown(self):
        logger.info('Starting graceful shutdown')
        await self._server.stop(5)


@async_run
async def init_afl_server():
    queue = janus.Queue()

    workspace = Workspace(queue.sync_q)
    aflpp = AFLPP(
        loop=asyncio.get_running_loop(),
        workspace=workspace,
        monitor_queue=queue,
        aflpp_proc=AFLProcess(workspace=workspace),
    )
    server = AFLPPServer(aflpp=aflpp)

    await server.run()


if __name__ == '__main__':
    init_afl_server()
