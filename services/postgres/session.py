from typing import Iterator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from config import PostgresCfg

engine = create_async_engine(
    url=PostgresCfg().url,
    future=True,
    echo=True
)

async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_db() -> Iterator[AsyncSession]:
    session: AsyncSession = async_session()
    try:
        yield session
        await session.commit()
    except Exception as exc:
        await session.rollback()
        raise exc
    finally:
        await session.close()
