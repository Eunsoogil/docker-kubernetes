import asyncio
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text, Row
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from .config.database import engine, get_session, async_session
from .config.model import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_VERSION = '/api/v1'


@app.on_event('startup')
async def startup_event():
    await asyncio.sleep(3)
    async with engine.begin() as conn:
        await conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {metadata.schema}"))
        # await conn.run_sync(metadata.drop_all)
        await conn.run_sync(metadata.create_all)

    async with async_session() as session:
        rows = await get_datas_from_database(session)
        if len(rows) == 0:
            await insert_default_datas(session)


@app.get('/health')
async def health():
    return 200


@app.get(f'{API_VERSION}/datas')
async def get_datas(
    session: AsyncSession = Depends(get_session)
):
    return list(map(lambda d: d[0], await get_datas_from_database(session)))


async def get_datas_from_database(session: AsyncSession):
    result = await session.execute(select(Test))
    return result.fetchall()


async def insert_default_datas(session: AsyncSession):
    session.add_all([
        Test(data='default data1'),
        Test(data='default data2')
    ])
    await session.commit()
