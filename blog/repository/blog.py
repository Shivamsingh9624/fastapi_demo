from ..database import get_db
from fastapi import Depends, HTTPException, status
from .. import schemas, models
from sqlalchemy.orm import Session


def get_all(db: Session):
	all_blog = db.query(models.Blog).all()
	return all_blog


def create(request: schemas.Blog, db: Session = Depends(get_db)):
	new_blog = models.Blog(title=request.title, body=request.body, nickname=request.nickname)
	db.add(new_blog)
	db.commit()
	db.refresh(new_blog)
	return new_blog


def delete(id, db: Session = Depends(get_db)):
	blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
	db.commit()
	return "Blog Deleted Sucessfully"


def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
	blog = db.query(models.Blog).filter(models.Blog.id == id)
	if not blog:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
							detail=f"blog with the id {id} is not avilable please try again")
	blog.update(request.dict())
	db.commit()
	return "blog updated Sucessfully"


def show(id: int, db: Session = Depends(get_db)):
	shw_blg = db.query(models.Blog).filter(models.Blog.id == id).first()
	if not shw_blg:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
							detail=f"blog with the id {id} is not avilable please try again")
	return shw_blg
