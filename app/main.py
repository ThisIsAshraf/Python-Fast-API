from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, votes

models.Base.metadata.create_all(bind=engine)


app = FastAPI();

print()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(votes.router)

# Test Route
@app.get("/")
async def root():
    return {"message": "Bismillahir Rahmanir Rahmin"}
