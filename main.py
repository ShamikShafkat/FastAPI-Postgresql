from fastapi import FastAPI,Depends
from routes.route import router
import models.model
from sqlalchemy.orm import Session
from config.database import engine,get_db
from typing import Annotated

models.model.Base.metadata.create_all(bind=engine)
db_dependency = Annotated[Session,Depends(get_db)]

app =  FastAPI()

app.include_router(router)