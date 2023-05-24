from sqlalchemy import Column, Text, Integer, DATE, JSON

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
    answer = Column(Text, nullable=False)
    question = Column(Text, nullable=False)
    airdate = Column(DATE, nullable=False)
