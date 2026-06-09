from sqlalchemy.orm import Session
from app.db.models import Category, Book

def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

def get_categories(db: Session):
    return db.query(Category).all()

def create_category(db: Session, title: str):
    db_category = Category(title=title)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def update_category(db: Session, category_id: int, title: str):
    category = get_category(db, category_id)
    if category:
        category.title = title
        db.commit()
        db.refresh(category)
    return category

def delete_category(db: Session, category_id: int):
    category = get_category(db, category_id)
    if category:
        db.delete(category)
        db.commit()
    return category

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def get_books(db: Session, category_id: int = None):
    query = db.query(Book)
    if category_id:
        query = query.filter(Book.category_id == category_id)
    return query.all()

def create_book(db: Session, title: str, description: str, price: float, category_id: int, url: str = ""):
    db_book = Book(title=title, description=description, price=price, category_id=category_id, url=url)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, book_id: int, title: str, description: str, price: float, url: str):
    book = get_book(db, book_id)
    if book:
        book.title = title
        book.description = description
        book.price = price
        book.url = url
        db.commit()
        db.refresh(book)
    return book

def delete_book(db: Session, book_id: int):
    book = get_book(db, book_id)
    if book:
        db.delete(book)
        db.commit()
    return book