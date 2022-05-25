from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def index():
	return {'data': {'Shiva': 18,
					 'course': 'computer'
					 }
			}


@app.get('/limit')
def blog(limit=20, published: bool = True):
	if published:
		return {'data': f'{limit} blogs are published'}
	else:
		return {'data': f'{limit} is limit in my blog'}


@app.get('/about')
def about():
	return 'This is about page'


# fetch id dynamically using id == id

@app.get('/id-name/{id}')
def id1(id: int):
	return {'id_is': id}


class Blog(BaseModel):
	title: str
	body: str
	published: Optional[bool]


@app.post('/blog')
def demo_post(request: Blog):
	return f'this is {request.title} from post blog and last name is  {request.body}'
