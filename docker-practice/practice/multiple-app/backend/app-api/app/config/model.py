from .database import metadata
from .database import Base
from sqlalchemy import Column, BIGINT, VARCHAR


class Test(Base):
    __tablename__ = 'test'
    id = Column(BIGINT, primary_key=True)
    data = Column(VARCHAR(50), nullable=False)
