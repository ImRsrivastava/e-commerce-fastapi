from pydantic import BaseModel


class CategorySchema (BaseModel):
    name: str
    description: str
    is_active: bool
    created_by: int