from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import JSONResponse, PlainTextResponse
from routers import blog_get, blog_post,user, article, product
from db.models import Base
from db.database import engine
from exceptions import StoryException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get('/hello')
def index():
    return {"message": "Hello world!"}


@app.exception_handler(StoryException)
def story_exception_handler(request:Request, exc:StoryException):
    return JSONResponse(
        status_code=418,
        content={'detail': exc.name}
    )


# @app.exception_handler(HTTPException)
# def custom_handler(request:Request, exc:StoryException):
#     return PlainTextResponse(str(exc), status_code=status.HTTP_400_INTERNAL_SERVER_ERROR)

Base.metadata.create_all(engine)

origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
