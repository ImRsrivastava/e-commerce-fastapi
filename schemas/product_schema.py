from pydantic import BaseModel

# Based on each Shop, have multiple products, which will be connected through shop_id
class ProductSchema(BaseModel):
    shop_id: int
    category_id: int
    auth_id: int
    name: str
    description: str
    price: float
    stock: int
    image_url: str
    is_active: bool
