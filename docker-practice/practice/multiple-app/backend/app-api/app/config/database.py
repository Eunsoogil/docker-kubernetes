from .config import dbconfig
import sqlalchemy
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base


# Set up database
DATABASE_URL = "postgresql+asyncpg://{user}:{password}@{postgres_server}:{port}/{db}"
DATABASE_URL = DATABASE_URL.format(
    user=dbconfig.get('DB_USER'),
    password=dbconfig.get('DB_PASSWORD'),
    postgres_server=dbconfig.get('DB_HOST'),
    port=dbconfig.get('DB_PORT'),
    db=dbconfig.get('DB_NAME')
)
metadata = sqlalchemy.MetaData(schema=dbconfig.get('DB_SCHEMA'))

engine = create_async_engine(
    DATABASE_URL,
    # echo=True,
)

async_session = async_sessionmaker(
    engine, expire_on_commit=False
)

Base = declarative_base(metadata=metadata)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
