from fastapi import APIRouter,HTTPException,status,Depends
from sqlalchemy.orm import Session
from .. import schemas,database,models,token
from ..hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm


get_db  = database.get_db

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(),db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Invalid credentials entered')
    
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Incorrect password')
    
    access_token = token.create_access_token(data={"sub": user.email})
    #sub means “subject” (i.e., who the token is for {"sub": "riya@example.com"}).
    #it will be storing the user's email inside the token.
    return {"access_token":access_token, "token_type":"bearer"}