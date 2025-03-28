
# Import the files and libraries
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schema, utils
from fastapi import FastAPI, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session
from .. database import get_db

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

# Create User
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.UserCreateResponse)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    
    # Password Hash
    # hashed_password= pwd_context.hash(user.password)
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

# Get User by ID
@router.get('/{id}', response_model=schema.UserCreateResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} not found")
    return user