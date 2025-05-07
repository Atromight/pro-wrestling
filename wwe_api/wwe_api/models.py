from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from wwe_api.const import WeightClass
from wwe_api.db import Base


class Nickname(Base):
    __tablename__ = "tNickname"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    wrestler_id = Column(Integer, ForeignKey("tWrestler.id"))

    wrestler = relationship("Wrestler", back_populates="nicknames")


class Wrestler(Base):
    __tablename__ = "tWrestler"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    birth_date = Column(DateTime)
    world_titles = Column(Integer)
    weight_class = Column(Enum(WeightClass), nullable=False)
    active = Column(Boolean)
    debut = Column(Integer)

    nicknames = relationship("Nickname", back_populates="wrestler", cascade="all, delete")
