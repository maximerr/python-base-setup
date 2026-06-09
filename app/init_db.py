from app.db.db import engine, Base, SessionLocal
from app.db.models import Category, Book
from app.db.crud import create_category, create_book

Base.metadata.create_all(bind=engine)
db = SessionLocal()

cat1 = create_category(db, "Фантастика")
cat2 = create_category(db, "Программирование")

create_book(db, "Дюна", "Фрэнк Герберт", 1200.0, cat1.id)
create_book(db, "Солярис", "Станислав Лем", 950.0, cat1.id)

create_book(db, "Python Crash Course", "Введение в Python", 2000.0, cat2.id)
create_book(db, "Грокаем алгоритмы", "Алгоритмы", 1100.0, cat2.id)

db.close()