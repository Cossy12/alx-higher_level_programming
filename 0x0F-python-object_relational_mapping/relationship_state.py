#!/usr/bin/python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City

"""
 City model.
Inherits  SQLAlchemy Base and links to the MySQL table cities.
"""
class State(Base):
    """
 City model.
Inherits  SQLAlchemy Base and links to the MySQL table cities.
"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
