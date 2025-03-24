# Import the files and libraries
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from typing import List
from .. import models, schema, oauth2
from fastapi import FastAPI, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session
from .. database import get_db

router = APIRouter(
    prefix="/posts",
    tags=['Post']
)

# Get all Post
@router.get("/", response_model=List[schema.Post])
def test_post(db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    posts = db.query(models.Post).all()
    return posts

# Create Post
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.Post)
def create_post(post: schema.PostCreate, db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    # new_post = models.Post(title=post.title, content=post.content, published=post.published)
    print(current_user.email)
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

# Get Post by ID
@router.get("/{id}", response_model=schema.Post)
def get_post(id: int, db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with ID: {id} was not found")
    return post

        
# Delete Post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    deleted_post = db.query(models.Post).filter(models.Post.id == id)
    if deleted_post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} does not exists")
    deleted_post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Update Post
@router.put("/{id}", response_model=schema.Post)
def update_post(id: int, post: schema.PostCreate, db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    updated_post = post_query.first()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} does not exists")
    post_query.update(post.dict(),synchronize_session= False)
    db.commit()
    return post_query.first()
