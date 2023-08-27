import asyncio

import grpc
import janus
from grpc_health.v1 import health, health_pb2_grpc

from aflpp_server.aflpp import AFLPP
from aflpp_server.helper import async_run, cleanup_coroutines
from aflpp_server.logger import logger
from aflpp_server.process import AFLProcess
from aflpp_server.protoc.v1.aflpp_pb2_grpc import add_AFLPPServicer_to_server
from aflpp_server.settings import settings
from aflpp_server.v1.aflpp import AFLPPServicer
from aflpp_server.workspace import Workspace


class AFLPPServer:
    def __init__(self, aflpp: AFLPP):
        self._aflpp = aflpp
        self._server = grpc.aio.server()
        self._aflpp_servicer = AFLPPServicer(aflpp)
        self._health_servicer = health.HealthServicer()

        add_AFLPPServicer_to_server(servicer=self._aflpp_servicer, server=self._server)
        health_pb2_grpc.add_HealthServicer_to_server(servicer=self._health_servicer, server=self._server)

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
async def run_aflpp_server():
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
    run_aflpp_server()
