from pydantic import BaseModel, EmailStr

# Shop will be belongs to auth id, one auth user can have multiple shops.
class ShopCreateSchema (BaseModel):
    name: str
    email: EmailStr
    address: str
    contact: str
    is_active: bool

class ShopUpdateSchema (BaseModel):
    name: str
    email: EmailStr
    address: str
    contact: str

class ShopStatusUpdateSchema (BaseModel):
    is_active: bool