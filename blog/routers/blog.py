from  fastapi import APIRouter,Depends,status,HTTPException
from typing import List
from .. import database,schemas,models,oauth2
from sqlalchemy.orm import Session
from ..repository import blog


#NOTE: the function definition is in the blog file within the repository folder

#A router in FastAPI is a way to organize your code by grouping related routes together. 
router = APIRouter(
    tags=['Blogs'],  
    #tags --> heading for each section of routes given globally instead of assigning individually
    prefix='/blog'
    #The prefix in APIRouter is used to automatically add a common path segment to all the routes defined in that router.
)
get_db = database.get_db


#get all blogs
@router.get('/',response_model=List[schemas.ShowBlog])
#List[schemas.ShowBlog] --> send back a list of blog posts, and each one should look like a ShowBlog.
def all(db:Session = Depends(get_db), current_user: schemas.User=Depends(oauth2.get_current_user)):
   return blog.get_all(db)  #the function definition is in the blog file within the repository folder
 


#create blogs
@router.post('/',status_code=status.HTTP_201_CREATED)
#When someone makes a POST request to /blog, call the function below.
# Status code --> total responses are 200, so when a new blog will be created its code will be 201.
#HTTP status codes are 3-digit numbers that APIs use to communicate the result of a request—like success, errors, or missing data—to the client.

def create(request:schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User=Depends(oauth2.get_current_user)):
#db: Session = Depends(get_db) -->	A way to give that function a database connection
   return blog.create(request,db)



# Deleting a Blog
@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int,db:Session = Depends(get_db), current_user: schemas.User=Depends(oauth2.get_current_user)):
   return blog.destroy(id,db)


# Updating a Blog - a PUT request is typically used to completely update or replace an existing resource.
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def updated(id:int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User=Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)
    


# To get/view blogs using a specific id
@router.get('/{id}', response_model=schemas.ShowBlog)
def show(id:int,db: Session = Depends(database.get_db), current_user: schemas.User=Depends(oauth2.get_current_user)):
    return blog.show(id,db)