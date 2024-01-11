from fastapi import FastAPI
from routers import blog_get, blog_post
from routers import user
from db.models import Base
from db.database import engine

app = FastAPI()
app.include_router(user.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get('/')
def index():
    return {"message": "Hello world!"}


Base.metadata.create_all(engine)
