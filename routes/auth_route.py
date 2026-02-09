from fastapi import APIRouter
from starlette import status
from core.database import DB_Dependency
from schemas.auth_schema import AuthRegisterSchema, AuthLoginSchema
from services.auth_service import AuthService
from utils.response import success


router = APIRouter(
    prefix = '/auth',
    tags = [ "Auth-Route" ]
)


@router.post('/register', status_code = status.HTTP_201_CREATED)
async def register_auth ( db: DB_Dependency, auth_req: AuthRegisterSchema ):
    auth = AuthService.register_service ( db, auth_req )
    return success ( "Auth user has been registered", auth )


@router.post('/login', status_code = status.HTTP_200_OK)
async def login_auth (db: DB_Dependency, auth_req: AuthLoginSchema):
    token = AuthService.login_service( db, auth_req.email, auth_req.password )
    return success("Login successful", {"access_token": token, "token_type": "bearer"})

