from  datetime import timedelta,datetime,timezone
from typing import Optional
from jose import JWTError,jwt
from .import schemas

# TOKEN --> act like a digital id card

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"  
#All JWTs generated by this FastAPI app must be signed with the same SECRET_KEY. It is used to sign the token
ALGORITHM = "HS256" #hashing algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = 30 #token expiration time

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta (minutes=ACCESS_TOKEN_EXPIRE_MINUTES) #current time in UTC+adds the variable's time. token will expire in 30 mins from the moment it's created.
    to_encode.update({"exp": expire})  
    #exp -->  tells the system when the token should expire.
    #adding a new key-value pair to the token data: {"sub": "riya@example.com", "exp": 2025-04-20 14:55:00} 
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token:str,credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub") #sub means the email id
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception