from sqlalchemy import create_engine  
#creates a connection engine to your database.

from sqlalchemy.ext.declarative import declarative_base 
#declare mapping


from sqlalchemy.orm import sessionmaker 
#actually start talking to the database that lets you open database sessions to run queries and commit changes. 

import sqlalchemy



SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'  #sqlite --> file based database

engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False})  
#connect_args={"check_same_thread":False} -->  It allows FastAPI to access the SQLite database from multiple threads by disabling SQLite's single-thread check. 

SessionLocal = sessionmaker(bind=engine,autocommit = False,autoflush=False)
'''
bind=engine: Connect this session to the database engine you created.

autocommit=False: You have to manually call .commit() — gives you more control.

autoflush=False: Prevents automatic updates to the database before queries — you control when data is pushed.
'''

Base = sqlalchemy.orm.declarative_base()   #It creates a base class that your SQLAlchemy models (tables) will inherit from.

