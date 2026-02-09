from pydantic import BaseModel


class CategoryCreateSchema (BaseModel):
    name: str
    description: str
    is_active: bool = True
    created_by: int

class CategoryUpdateSchema (BaseModel):
    name: str
    description: str