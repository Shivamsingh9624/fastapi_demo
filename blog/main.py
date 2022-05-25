from fastapi import FastAPI
from . import models
from .database import engine
from . import routers

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(routers.user_router.router)
app.include_router(routers.blog_router.router)
app.include_router(routers.authentication.router)
