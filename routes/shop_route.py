from fastapi import APIRouter, HTTPException
from starlette import status
from core.database import DB_Dependency
from services.common_service import Auth_Dependency
from services.shop_service import ShopService
from utils.response import success
from schemas.shop_schema import ShopCreateSchema


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

@router.post( "/", status_code = status.HTTP_201_CREATED )
async def create_shop ( db: DB_Dependency, auth: Auth_Dependency, shop_req: ShopCreateSchema ):
    shop = ShopService.create_shop( db, auth, shop_req )
    return success( "Shop created successfully.", shop)