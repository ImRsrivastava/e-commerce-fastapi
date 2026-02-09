from pydantic import BaseModel, EmailStr

class AuthRegisterSchema (BaseModel):
    first_name: str
    last_name: str
    full_name: str
    email: EmailStr
    password: str
    is_active: bool = True

class AuthLoginSchema (BaseModel):
    email: EmailStr
    password: str