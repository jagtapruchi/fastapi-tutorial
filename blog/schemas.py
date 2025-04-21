from pydantic import BaseModel #it is the base class for all Pydantic models — like blueprints for what your data should look like.
from typing import List, Optional
#importing a module named schemas.py from the current package/directory/folder

#Note: PYdantic models are called as 'schemas'

#The `response_model` in FastAPI lets you choose what data to send back** in a response and hides anything extra. It supports abstraction.

#Note: SQLAlchemy doesn't know how to handle objects it alwyas expects a dictionary/keyword arguments. To counter this behaviour of SQLAlchemy models the 'orm_mode' is used so that it caan handle objects using . operator


#schemas are Python CLASSES that define the structure (and validation rules) for your data, usually using Pydantic.

class Blog(BaseModel):
    title: str
    body: str
    user_id: int
    #id is not mentioned here as id will database generated
    
    class Config():
        from_attributes = True
    

class User(BaseModel):
    name: str
    email: str
    password:str
    #id will be generated automatically
    
class UserSimple(BaseModel):
    name: str
    email: str  
    class Config():
        from_attributes = True  
    
class Login(BaseModel):
    username: str
    password: str

#response model: 
class ShowBlog(BaseModel): #acts a the response model
    title: str
    body: str
    creator: UserSimple
    class Config():
        from_attributes = True  #Don’t expect a dict. You’re going to be reading a database object with dot-access fields — act accordingly.

#response model:
class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[ShowBlog]
    class Config():
        from_attributes = True

#Schema for returning the JWT access token.
class Token(BaseModel):
    access_token: str #the token itself
    token_type: str #usually 'bearer'

#Used internally when decoding the token. username is optional.
class TokenData(BaseModel):
    email: Optional[str] = None


'''   
ORM --> Connectivity between python code & database 
ORM converts Python objects into database rows
Python class is a database table, attributes are columns in the db table and the objects in that class are rows in the database table
'''