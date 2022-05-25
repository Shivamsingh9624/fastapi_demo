from fastapi import APIRouter, Depends, HTTPException, status
from .. import database, schemas, models
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
	tags=['User'],
	prefix='/user'
)

get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.CreateUser, db: Session = Depends(get_db)):
	return user.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def show(id: int, db: Session = Depends(get_db)):
	return user.show(id, db)
