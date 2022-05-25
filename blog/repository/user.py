from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import database, schemas, models, hashing

get_db = database.get_db


def create(request: schemas.CreateUser, db: Session = Depends(get_db)):
	new_user = models.User(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password))
	db.add(new_user)
	db.commit()
	db.refresh(new_user)

	return new_user


def show(id: int, db: Session):
	user = db.query(models.User).filter(models.User.id == id).first()
	if not user:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
							detail=f"blog with the id {id} is not avilable please try again")
	return user
