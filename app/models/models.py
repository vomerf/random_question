from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, Text
from sqlalchemy.orm import declarative_base, declared_attr


class Base:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)


class RandomQuestion(Base):
    __tablename__ = 'random_question'

    id_question = Column(Integer(), unique=True, nullable=False)
    answer = Column(Text)
    question = Column(Text)
    airdate = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
