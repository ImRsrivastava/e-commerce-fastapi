from pydantic import BaseModel

# Based on each Shop, have multiple products, which will be connected through shop_id
class ProductCreateSchema(BaseModel):
    shop_id: int
    category_id: int
    auth_id: int
    name: str
    description: str
    price: float
    stock: int
    is_active: bool


class ProductUpdateSchema (BaseModel):
    shop_id: int
    category_id: int
    name: str
    description: str
    price: float
    stock: int
    image_url: str

class ProductImageSchema (BaseModel):
    image_url: str