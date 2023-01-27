from sqlalchemy import Column, Integer, Float, Boolean, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from src.db import DeclarativeBase


class MlData(DeclarativeBase):
    __tablename__ = "ml_data"
    id = Column(Integer, primary_key=True)
    time = Column(DateTime)
    value = Column(Float)
    error = Column(Boolean)
    warn = Column(Boolean)
    table_id = Column(Integer, ForeignKey("ml_tables.id"))

class MlTable(DeclarativeBase):
    __tablename__ = "ml_tables"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    db_id = Column(String)
    data = relationship("MlData")