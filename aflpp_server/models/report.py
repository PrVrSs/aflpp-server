from typing import AsyncIterator, Optional, Self

from sqlalchemy import String, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from ..exceptions import AFLPPServerException
from .base import Base


class Report(Base):
    __tablename__ = 'report'

    id: Mapped[int] = mapped_column('id', autoincrement=True, nullable=False, unique=True, primary_key=True)
    bug_type: Mapped[str] = mapped_column('bug_type', String(), nullable=False)
    raw: Mapped[str] = mapped_column('raw', String(), nullable=False)
    detail: Mapped[str] = mapped_column('detail', String(), nullable=False)

    @classmethod
    async def select_all(cls, session: AsyncSession) -> AsyncIterator[Self]:
        stream = await session.stream_scalars(select(cls).order_by(cls.id))
        async for row in stream:
            yield row

    @classmethod
    async def select_by_id(
        cls,
        session: AsyncSession,
        idx: int,
    ) -> Optional[Self]:
        return await session.scalar(
            select(cls)
            .where(cls.id == idx)
            .order_by(cls.id)
        )

    @classmethod
    async def add(cls, session: AsyncSession, bug_type: str, detail: str, raw: str) -> Self:
        report = Report(bug_type=bug_type, raw=raw, detail=detail)
        session.add(report)
        await session.commit()

        new_report = await cls.select_by_id(session, report.id)
        if new_report is None:
            raise AFLPPServerException

        return new_report
