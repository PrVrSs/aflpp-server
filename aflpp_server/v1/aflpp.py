import grpc

from aflpp_server.aflpp import AFLPP
from aflpp_server.db import get_session
from aflpp_server.models import Report
from aflpp_server.protoc.v1.aflpp_pb2 import (
    ReportRequest,
    ReportResponse,
    StartRequest,
    StartResponse,
    StatisticRequest,
    StatisticResponse,
    StopRequest,
    StopResponse,
)
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
        return StopResponse(success=await self._aflpp.stop())

    async def stats(self, request: StatisticRequest, context: grpc.aio.ServicerContext) -> StatisticResponse:
        return StatisticResponse(**(await self._aflpp.stats()))

    async def reports(self, request: ReportRequest, context: grpc.aio.ServicerContext) -> ReportResponse:
        async with get_session() as session:
            async for report in Report.select_all(session=session):
                yield ReportResponse(
                    raw=report.raw,
                    bug_type=report.bug_type,
                    detail=report.detail,
                )
