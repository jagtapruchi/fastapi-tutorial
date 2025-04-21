
# to run:  uvicorn blog.main:app --reload

from fastapi import FastAPI
from . database import engine
from .routers import blog, users,authentication
from . import models
#from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(engine)

#A router is just a way to define and group API routes separately, and then include them in your main app.
app.include_router(blog.router)
app.include_router(users.router)
app.include_router(authentication.router)

#from typing import List
#from fastapi import FastAPI,Depends,status,Response,HTTPException
#from . import models,schemas
#import everything from the models & schemas files in this folder

#from . hashing import Hash  #From the hashing.py file, import the Hash class
#from sqlalchemy.orm import Session
'''
SESSION -->  A temporary connection to the database, where you can send and receive data.
Knows how to talk to the database
Lets you add, read, update, delete data
Keeps track of changes
Must be opened before use, and closed after — just like opening and closing a file
'''

#from . database import engine,get_db 
#import engine from database file 

#from . routers import blog, users
#importing the routers from blog & users file


#def get_db():
    #db = SessionLocal()  #creates a new database session
    #try:
        #yield db   #give it to whoever called this function
    #finally:
        #db.close()  #Make sure it's closed afterward (whether or not there's an error)


#Create blog
#@app.post('/blog',status_code=status.HTTP_201_CREATED,tags=['blogs'])
#When someone makes a POST request to /blog, call the function below.
# Status code --> total responses are 200, so when a new blog will be created its code will be 201.
#HTTP status codes are 3-digit numbers that APIs use to communicate the result of a request—like success, errors, or missing data—to the client.

#def create(request:schemas.Blog, db: Session = Depends(get_db)):
#db: Session = Depends(get_db) -->	A way to give that function a database connection

   #new_blog = models.Blog(title=request.title,body=request.body,user_id #= request.user_id)   
   #This refers to the Blog model that you defined in your models.py file. Here, id will database generated
   
   #db.add(new_blog)   #This is an SQLAlchemy command that adds the new blog post (new_blog) to the session.

   #db.commit() #This is where the changes are actually saved to the database.
   
   #db.refresh(new_blog)  #The refresh() function reloads the new_blog object from the database, so it has the updated data, including the ID assigned by the database.
   
   #return new_blog



# Deleting a Blog
#@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=#['blogs'])
#def destroy(id,db:Session = Depends(get_db)):
    #blog = db.query(models.Blog).filter(models.Blog.id == id)
    #if not blog.first():
       # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, #detail=f"Blog with id {id} not found")
    #blog.delete(synchronize_session=False)
#synchronize_session=False --> it means when it gets deleted it doesn't update the database immediately but the updates take place when we perform the db.commit()
    #db.commit()
    


# Updating a Blog - a PUT request is typically used to completely update or replace an existing resource.
#@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=#['blogs'])
#def updated(id, request: schemas.Blog, db: Session = Depends(get_db)):
    #blog = db.query(models.Blog).filter(models.Blog.id == id)
    #if not blog.first():
        #raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, #detail=f"Blog with id {id} is not found")
    #else:
        #blog.update({'title':request.title, 'body':request.body})
    #db.commit()
   # return 'updated'



# To view/get all the blogs from the database
#@app.get('/blog',response_model=List[schemas.ShowBlog],tags=['blogs'])
#List[schemas.ShowBlog] --> send back a list of blog posts, and each one should look like a ShowBlog.

#def all(db:Session = Depends(get_db)):
    #blogs = db.query(models.Blog).all()  #Runs SELECT * FROM blogs and gets all rows
    #return blogs




# To get/view blogs using a specific id
#@app.get('/blog/{id}', response_model=schemas.ShowBlog,tags=['blogs'])
#def show(id,response: Response,db: Session = Depends(get_db)):
    #blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    
    #handles the status code and error message when unavailable id is entered
    #if not blog:        
        #Using HTTPException
        #raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, #detail= f'Blog with id {id} is not available')
    
        #Without HTTPException
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {'detail':f'Blog with id {id} is not available'}
    #return blog













# Create User
#@app.post('/user',response_model=schemas.ShowUser,tags=['users'])
#def create_user(request: schemas.User,db: Session = Depends(get_db)):
     
     #new_user = models.User(name=request.name,email=request.email,#password=Hash.bcrypt(request.password))
     #Call the bcrypt method inside the Hash class that's being imported
     #db.add(new_user)
     #db.commit()
     #db.refresh(new_user) 
     #return new_user
 
 
# To get/view user using a specific id
#@app.get('/user/{id}',response_model=schemas.ShowUser,status_code=200,#tags=['users'])
#def show_users(id,response: Response,db:Session = Depends(get_db)):
    #user = db.query(models.User).filter(models.User.id == id).first()
    #if not user:
        #raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,#detail=f"User with id {id} is not available")
    #return user
