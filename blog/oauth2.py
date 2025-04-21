from fastapi import Depends,HTTPException,status
from . import token
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login") #it authenticate and gets a JWT, sends a request to /login.

def get_current_user(data: str = Depends(oauth2_scheme)): 
    
    #protected endpoints will use this line "token: str = Depends(oauth2_scheme)" to automatically grab the token from the Authorization header like: Authorization: Bearer <token>

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    return token.verify_token(data,credentials_exception)