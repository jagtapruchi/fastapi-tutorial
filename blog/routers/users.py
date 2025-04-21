from fastapi import APIRouter,Response,HTTPException,status,Depends
from .. import database,schemas,models
from sqlalchemy.orm import Session
from ..repository import users

#NOTE: the function definition is in the users file within the repository folder


#A router in FastAPI is a way to organize your code by grouping related routes together. 
router = APIRouter(
    tags=['Users'],
    prefix= '/user'
)


# Create User
@router.post('/',response_model=schemas.ShowUser)
def create_user(request: schemas.User,db: Session = Depends(database.get_db)):
    return users.create(request,db) #the function definition is in the users file within the repository folder
 
 
 
# To get/view user using a specific id
@router.get('/{id}',response_model=schemas.ShowUser,status_code=200)
def show_users(id,response: Response,db:Session = Depends(database.get_db)):
    return users.view(id,db)
