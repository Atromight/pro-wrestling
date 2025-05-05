from sqlalchemy import Boolean, Column, DateTime, Enum, Integer, String

from wwe_api.const import WeightClass
from wwe_api.db import Base

class Wrestler(Base):
    __tablename__ = "tWrestler"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    birth_date = Column(DateTime)
    world_titles = Column(Integer)
    weight_class = Column(Enum(WeightClass), nullable=False)
    active = Column(Boolean)
    debut = Column(Integer)
