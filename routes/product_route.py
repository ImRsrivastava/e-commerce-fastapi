from fastapi import APIRouter, HTTPException
from starlette import status
from core.database import DB_Dependency
from services.common_service import Auth_Dependency
from utils.response import success
from schemas.product_schema import ProductCreateSchema, ProductUpdateSchema, ProductImageSchema


router = APIRouter(
    prefix = "/product",
    tags = ["Product Routes"]
)


# GET     /product/                  → Get all products
@router.get( "/", status_code = status.HTTP_200_OK )
async def get_all_products ( db: DB_Dependency, auth: Auth_Dependency ):
    if auth is None:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="Unauthorized access!")
    products = None
    return success( "All Products retrieved successfully", products )


# POST    /product/                  → Create product
@router.post( "/", status_code = status.HTTP_201_CREATED )
async def create_product ( db: DB_Dependency, auth: Auth_Dependency, product_req: ProductCreateSchema ):
    if auth is None:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="Unauthorized access!")
    product = None
    return success( "Product created successfully" )


# POST    /product/{}/upload_image                  → Upload product
@router.post( "/product/{product_id}/upload_image", status_code= status.HTTP_201_CREATED )
async def upload_images ( db: DB_Dependency, auth: Auth_Dependency, image_req: ProductImageSchema ):
    if auth is None:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="Unauthorized access!")
    product = None
    return success( "Product images uploaded successfully" )


# GET     /product/{product_id}      → Get product by id
@router.get( "/{product_id}", status_code = status.HTTP_200_OK )
async def get_product_by_id ( db: DB_Dependency, auth: Auth_Dependency, product_id: int ):
    if auth is None:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="Unauthorized access!")
    product = None
    return success( "Product retrieved by Product ID successfully", product )


# PUT     /product/{product_id}      → Update product
@router.put( "/{product_id}", status_code = status.HTTP_200_OK )
async def update_product ( db: DB_Dependency, auth: Auth_Dependency, product_id: int, product_req: ProductUpdateSchema ):
    if auth is None:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="Unauthorized access!")
    product = None
    return success( "Product updated successfully")


# DELETE  /product/{product_id}      → Delete product
@router.delete( "/{product_id}", status_code = status.HTTP_200_OK )
async def delete_product ( db: DB_Dependency, auth: Auth_Dependency, get_product_by_id: int):
    if auth is None:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="Unauthorized access!")
    product = None
    return success( "Product deleted successfully" )