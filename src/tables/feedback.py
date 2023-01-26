from sqlalchemy import Column, Integer, String

from src.db import DeclarativeBase


class Feedback(DeclarativeBase):
    __tablename__ = "feedbacks"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    description = Column(String)