from app.db.db import SessionLocal
from app.db.crud import get_categories, get_books

db = SessionLocal()

categories = get_categories(db)
print("Категории:")
for cat in categories:
    print(f"- {cat.title}")

books = get_books(db)
print("\nКниги:")
for book in books:
    print(f"- {book.title} | {book.price} руб. | Категория ID: {book.category_id}")

db.close()