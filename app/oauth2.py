from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schema, database, models
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

oauth2_Scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = "1c3ce633850db8aadf37e369354a16ea694e1afabd750a6f8aa5af955a44a099"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
    

def verify_access_token(token: str, credentials_exception):
    try:
        
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        
        id: str = payload.get("user_id")
        
        if id is None:
            raise credentials_exception
        token_data = schema.TokenData(id=id)
    except JWTError:
        raise credentials_exception
    return token_data

def get_current_user(token: str = Depends(oauth2_Scheme), db: Session = Depends(database.get_db)):
    credentails_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Colud not validate the credentials", headers={"WWW-Authenticate": "Bearer"})
    
    token = verify_access_token(token, credentails_exception)
    
    user = db.query(models.User).filter(models.User.id == token.id).first()
    
    return user