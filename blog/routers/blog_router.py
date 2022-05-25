from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database, models
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
	tags=['Blog'],
	prefix='/blog'
)

get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db)):
	return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
	return blog.create(request, db)


@router.get('/{id}', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db)):
	return blog.show(id, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destory(id: int, db: Session = Depends(get_db)):
	return blog.delete(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
	return blog.update(id, request, db)
