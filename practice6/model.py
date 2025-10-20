from fastapi import Form
from pydantic import BaseModel
from typing import List, Optional


class Item(BaseModel):
    item: str
    status: str


class Todo(BaseModel):
    id: Optional[int]
    item: str
    status: Optional[str]

    @classmethod
    def as_form(cls, item: str = Form(...)):
        return cls(id=None, item=item, status=None)

    class Config:
        Schema_extra = {
            "Example": {
                "id": 1,
                "item": "Example schema!"
            }
        }


class TodoItem(BaseModel):
    item: str
    class Config:
        schema_extra = {
            "example": {
                "item": "Read the next chapter of the book"
            }
        }


class TodoItems(BaseModel):
    todos: List[TodoItem]
    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Example schema 1!"
                    },
                    {
                        "item": "Example schema 2!"
                    }
                ]
            }
        }