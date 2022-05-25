from typing import Optional

from pydantic import BaseModel


class Blog(BaseModel):
	title: str
	body: str
	nickname: str


class ShowBlog(BaseModel):
	title: str

	class Config():
		orm_mode = True


class CreateUser(BaseModel):
	name: str
	email: str
	password: str


class ShowUser(BaseModel):
	name: str
	email: str

	class Config():
		orm_mode = True


class Login(BaseModel):
	username: str
	password: str

	class Config():
		orm_mode = True


# JWT
class Token(BaseModel):
	access_token: str
	token_type: str


class TokenData(BaseModel):
	username: Optional[str] = None
