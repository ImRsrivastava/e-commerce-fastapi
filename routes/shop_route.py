from fastapi import APIRouter, HTTPException
from starlette import status
from core.database import DB_Dependency
from services.common_service import Auth_Dependency
from services.shop_service import ShopService
from utils.response import success
from schemas.shop_schema import ShopCreateSchema, ShopUpdateSchema, ShopStatusUpdateSchema


router = APIRouter (
    prefix = "/shop",
    tags = [ "Shop-Routes"]
)

@router.get( '/', status_code = status.HTTP_200_OK )
async def get_all_shops ( db: DB_Dependency, auth: Auth_Dependency ):
    if auth is None:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="Unauthorized access!")
    shops = ShopService.get_all_shops( db, auth )
    if not shops:
        raise HTTPException ( status_code = status.HTTP_404_NOT_FOUND, detail = "No Shops Found!" )
    return success( "All shops retrieved successfully.", shops )

@router.post( "/", status_code = status.HTTP_201_CREATED )
async def create_shop ( db: DB_Dependency, auth: Auth_Dependency, shop_req: ShopCreateSchema ):
    if auth is None:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="Unauthorized access!")
    shop = ShopService.create_shop( db, auth, shop_req )
    return success( "Shop created successfully.", shop)

@router.get('/{shop_id}', status_code = status.HTTP_200_OK )
async def edit_shop ( db: DB_Dependency, auth: Auth_Dependency, shop_id: int ):
    if auth is None:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="Unauthorized access!")
    shop = ShopService.edit_shop( db, auth, shop_id )
    if shop is None:
        raise HTTPException ( status_code = status.HTTP_404_NOT_FOUND, detail = "Shop with this id does not exist!" )
    return success( "Shop found successfully.", shop )

@router.put( '/{shop_id}', status_code = status.HTTP_200_OK )
async def update_shop ( db: DB_Dependency, auth: Auth_Dependency, shop_id: int, shop_req: ShopUpdateSchema ):
    if auth is None:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="Unauthorized access!")
    shop = ShopService.update_shop( db, auth, shop_id, shop_req )
    if shop is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Shop with this id does not exist!")
    return success( "Shop updated successfully.", shop )

@router.put( "/status/{shop_id}", status_code = status.HTTP_200_OK )
async def update_shop_status ( db: DB_Dependency, auth: Auth_Dependency, shop_id: int, shop_req: ShopStatusUpdateSchema ):
    if auth is None:
        raise HTTPException ( status_code = status.HTTP_401_UNAUTHORIZED, detail="Unauthorized access!" )
    shop = ShopService.update_shop_status( db, auth, shop_id, shop_req )
    if shop is None:
        raise HTTPException ( status_code = status.HTTP_404_NOT_FOUND, detail="Shop with this id does not exist!" )
    return success( "Shop status updated successfully.", shop )

@router.delete( "/{shop_id}", status_code = status.HTTP_200_OK )
async def delete_shop ( db: DB_Dependency, auth: Auth_Dependency, shop_id: int ):
    if auth is None:
        raise HTTPException ( status_code = status.HTTP_401_UNAUTHORIZED, detail="Unauthorized access!" )
    shop = ShopService.delete_shop( db, auth, shop_id )
    if shop is None:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail="Shop with this id does not exist!" )
    return success( "Shop deleted successfully." )