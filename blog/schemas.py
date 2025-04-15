from fastapi import FastAPI
from pydantic import BaseModel
#importing a module named schemas.py from the current package/directory/folder

#Note: PYdantic models are called as 'schemas'

app = FastAPI()

#schemas are Python CLASSES that define the structure (and validation rules) for your data, usually using Pydantic.

class Blog(BaseModel):
    title: str
    body: str
    #id is not mentioned here as id will database generated
    
#The `response_model` in FastAPI lets you choose what data to send back** in a response and hides anything extra. It supports abstraction.
class ShowBlog(BaseModel): #acts a the response model
    title: str
    body: str
    class Config():
        from_attributes = True  #Don’t expect a dict. You’re going to be reading a database object with dot-access fields — act accordingly.

#Note: SQLAlchemy doesn't know how to handle objects it alwyas expects a dictionary/keyword arguments. To counter this behaviour of SQLAlchemy models the 'orm_mode' is used so that it caan handle objects using . operator

class Users(BaseModel):
    name: str
    email: str
    password:str
    #id will be generated automatically
    
#response model:
class ShowUser(BaseModel):
    name: str
    email: str
    class Config():
        from_attributes = True
    

'''   
ORM --> Connectivity between python code & database 
ORM converts Python objects into database rows
Python class is a database table, attributes are columns in the db table and the objects in that class are rows in the database table
'''