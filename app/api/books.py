from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db.db import get_db
from app.db import crud
from app import schemas

router = APIRouter(prefix="/books", tags=["books"])

@router.get("/", response_model=List[schemas.BookResponse])
def read_books(category_id: Optional[int] = None, db: Session = Depends(get_db)):
    return crud.get_books(db, category_id)

@router.get("/{book_id}", response_model=schemas.BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/", response_model=schemas.BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    category = crud.get_category(db, book.category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return crud.create_book(db, book.title, book.description, book.price, book.category_id, book.url)

@router.put("/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    category = crud.get_category(db, book.category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    db_book = crud.update_book(db, book_id, book.title, book.description, book.price, book.url)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.delete_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return None