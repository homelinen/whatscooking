from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import HSTORE

from whatscooking.database import Base


class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    ingredients = Column(HSTORE, nullable=False)

    def __init__(self, name, ingredients={}):
        self.name = name
        self.ingredients = ingredients
