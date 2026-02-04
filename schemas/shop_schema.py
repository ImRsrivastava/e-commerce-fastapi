from pydantic import BaseModel

# Shop will be belongs to auth id, one auth user can have multiple shops.
class ShopSchema (BaseModel):
    name: str
    email: float
    owner: int
    address: str
    contact: int
    is_active: bool