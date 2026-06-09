from pydantic import BaseModel, ConfigDict
from typing import Optional

class CategoryBase(BaseModel):
    title: str

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class BookBase(BaseModel):
    title: str
    description: str
    price: float
    url: Optional[str] = ""
    category_id: int

class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int
    model_config = ConfigDict(from_attributes=True)