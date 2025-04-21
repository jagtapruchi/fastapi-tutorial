from passlib.context import CryptContext  #"password hashing manager" from the PassLib library.

pwd_cxt = CryptContext(schemes=["bcrypt"],deprecated="auto")
#bcrypt is the algorithm for hashing passwords.
# deprecated="auto" --> If better hashes come later, auto-detect and support rehashing old ones.  New users will get their passwords hashed using new hash but old users still have bcrypt-hashed passwords in the database

class Hash():
    def bcrypt(password: str):
        return pwd_cxt.hash(password)
    
    def verify(hashed_password,plain_password):
        return pwd_cxt.verify(plain_password,hashed_password)