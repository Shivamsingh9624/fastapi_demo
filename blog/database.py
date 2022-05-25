from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE = r'sqlite:///C:\Users\Shail\PycharmProjects\fastapi_demo\blog\blog.db'
engine = create_engine(SQLALCHEMY_DATABASE, connect_args={"check_same_thread": False})

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()
