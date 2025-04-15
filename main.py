from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn
app = FastAPI()    #instance of fastapi

@app.get('/')
def index(): #path operation function
    return {'data':'blog list'}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(request:Blog):  #request --> variable storing Blog object,  Blog --> object created with the body mentioned above
    return {'data':f"Blog is created with title as {request.title}"} 

'''
@app.get('/blog')
def INDEX(limit=20,published:bool=True,sort:Optional[str] = None):
    #fetch only no of (limit) published blogs example: 70/80/3/4/23,etc from the list of all published blogs
    if published:   #if query parameter is published=true
        return {'data': f'{limit} published blogs from db'}
    else:   #if query parameter is published=false
        return {'data': f'{limit} blogs from db'}
'''
# @app --> path operation decorator
# get() --> operation
# '/' --> path

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id:int): #path operation function
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data':{'1','2'}}

#to start server on  new localhost: 9000
#if __name__ == "__main__":
#    uvicorn.run(app,host="127.0.0.1",port=9000)