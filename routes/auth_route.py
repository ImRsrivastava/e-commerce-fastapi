from fastapi import APIRouter
from starlette import status
from core.database import DB_Dependency
from schemas.auth_schema import AuthSchema
from services.auth_service import AuthService
from utils.response import success, error


router = APIRouter(
    prefix = '/auth',
    tags = [ "Auth-Route" ]
)


@router.post('/register', status_code = status.HTTP_201_CREATED)
async def register_auth ( db: DB_Dependency, auth_req: AuthSchema ):
    auth = AuthService.register_service ( db, auth_req )
    return success ( "Auth user has been registered", auth )