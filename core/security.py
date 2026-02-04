from core.config import settings
from passlib.context import CryptContext



bcryptContext = CryptContext( schemas = ["bcrypt"], deprecated = "auto" )

# Password Hashed
async def hash_password (password: str) -> str:
    return bcryptContext.hash(password)

async def verify_password (plain_password: str, hashed_password: str) -> bool:
    return bcryptContext.verify(plain_password, hashed_password)
