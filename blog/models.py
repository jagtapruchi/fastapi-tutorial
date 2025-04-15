from sqlalchemy import Column,Integer,String
from . database import Base  #from database.py import the declarative base class

#Note: SQLAlchemy models are called as 'models'

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    body = Column(String)

class Users(Base):
    __tablename__ = 'Users'
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)