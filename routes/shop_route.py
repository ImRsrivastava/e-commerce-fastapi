from fastapi import APIRouter, HTTPException
from starlette import status
from core.database import DB_Dependency
from services.common_service import Auth_Dependency
from services.shop_service import ShopService
from utils.response import success


router = APIRouter (
    prefix = "/shop",
    tags = [ "Shop-Routes"]
)

@router.get( '/', status_code = status.HTTP_200_OK )
async def get_all_shops ( db: DB_Dependency, auth: Auth_Dependency ):
    shops = ShopService.get_all_shop( db, auth )
    if not shops:
        raise HTTPException ( status_code = status.HTTP_404_NOT_FOUND )
    return success( "All shops retrieved successfully.", shops )