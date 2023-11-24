#!/usr/bin/python3
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

"""
 City model.
Inherits  SQLAlchemy Base and links to the MySQL table cities.
"""

Base = declarative_base()

"""
 City model.
Inherits  SQLAlchemy Base and links to the MySQL table cities.
"""
class City(Base):
    """
 City model.
Inherits  SQLAlchemy Base and links to the MySQL table cities.
"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
