from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from starlette import status

from core.config import settings
from datetime import timedelta, datetime
from jose import jwt, JWTError

bcryptContext = CryptContext( schemes = ["bcrypt"], deprecated = "auto" )
oauth2Beare = OAuth2PasswordBearer( tokenUrl = settings.JWT_TOKE_URL)

# Password Hashed
def hash_password (password: str) -> str:
    return bcryptContext.hash(password)


def verify_password (plain_password: str, hashed_password: str) -> bool:
    return bcryptContext.verify(plain_password, hashed_password)


def create_access_token ( data: dict ):
    to_encode = data.copy()
    to_encode['iat'] = datetime.utcnow()        # issued-at time. It is mandatory as per industry best practice
    expire = datetime.utcnow() + timedelta(minutes = settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode['exp'] = expire       # Add expiration time

    # Encode JWT token
    encoded_jwt = jwt.encode( to_encode, settings.JWT_SECRET, algorithm = settings.JWT_ALGORITHM )
    return encoded_jwt

def verify_access_token ( token: str ):
    try:
        payload = jwt.decode( token, settings.JWT_SECRET, algorithms = settings.JWT_ALGORITHM )
        return payload
    except JWTError:
        raise HTTPException ( status_code = status.HTTP_401_UNAUTHORIZED )
