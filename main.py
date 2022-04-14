import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from fastapi import FastAPI, HTTPException, status


from schema import Book as SchemaBook
from schema import Author as SchemaAuthor

from schema import Book
from schema import Author

from models import Book as ModelBook
from models import Author as ModelAuthor

import os
from dotenv import load_dotenv


load_dotenv('.env')


app = FastAPI()

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

#database = SessionLocal()

# http method get of the route root
@app.get('/')
async def root():
    return {f'Message: Hello fastAPI'}

# http method post for book
@app.post('/book/', response_model=SchemaBook, status_code=status.HTTP_200_OK)
async def book(book: SchemaBook):
    db_book = ModelBook(title=book.title, rating=book.rating, author_id=book.author_id)
    db.session.add(db_book)
    db.session.commit()
    return db_book

# http method get book route
@app.get('/book/')
async def book():
    book = db.session.query(ModelBook).all()
    return book


# http method post for author
@app.post('/author/', response_model=SchemaAuthor, status_code=status.HTTP_200_OK)
async def author(author:SchemaAuthor):
    db_author = ModelAuthor(name=author.name, age=author.age)
    db.session.add(db_author)
    db.session.commit()
    return db_author


# http method get for author
@app.get('/author/')
async def author():
    author = db.session.query(ModelAuthor).all()
    return author

# To run locally

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)