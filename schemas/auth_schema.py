from pydantic import BaseModel

class AuthSchema (BaseModel):
    first_name: str
    last_name: str
    full_name: str
    email: str
    password: str
    is_active: bool