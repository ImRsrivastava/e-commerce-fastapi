from typing import List
from fastapi import APIRouter, HTTPException, UploadFile, File
from starlette import status
from core.database import DB_Dependency
from services.common_service import Auth_Dependency
from utils.response import success
from schemas.product_schema import ProductCreateSchema, ProductUpdateSchema, ProductImageSchema
from services.product_service import ProductService
from utils.image_handler import save_product_image


router = APIRouter(
    prefix = "/product",
    tags = ["Product Routes"]
)

############### Route List ###############
    # GET       /product                                → Get all Products
    # POST      /product                                → Create Product
    # POST      /product/{product_id}/upload_image      → Upload Product Images
    # GET       /product/{product_id}                   → Get Product by Product ID
    # PUT       /product/{product_id}                   → Update Product by Product ID
    # DELETE    /product/{product_id}                   → Delete product by Product ID
    # DELETE    /product/{product_id}/{image_id}        → Delete product image by Product ID & Image ID

    # Advanced Product Features Routes
    # GET       /product/?name=iphone
    # GET       /product/?min_price=100&max_price=500
    # GET       /product/?category_id=1
    # GET       /product/?sort=price_asc


# GET     /product/                  → Get all products
@router.get( "/", status_code = status.HTTP_200_OK )
async def get_all_products (
                db: DB_Dependency,
                auth: Auth_Dependency,
                name: str | None = None,
                min_price: float | None = None,
                max_price: float | None = None,
                category_id: int | None = None,
                sort: str | None = None
        ):
    if auth is None:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="Unauthorized access!")
    products = ProductService.get_all_products( db, auth, name, min_price, max_price, category_id, sort )
    return success( "All Products retrieved successfully", products )


# GET     /product/{product_id}      → Get product by id
@router.get( "/{product_id}", status_code = status.HTTP_200_OK )
async def get_product_by_id ( db: DB_Dependency, auth: Auth_Dependency, product_id: int ):
    if auth is None:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="Unauthorized access!")
    product = ProductService.get_product_by_id ( db, auth, product_id )
    return success( "Product retrieved by Product ID successfully", product )


# POST    /product/                  → Create product
@router.post( "/", status_code = status.HTTP_201_CREATED )
async def create_product ( db: DB_Dependency, auth: Auth_Dependency, product_req: ProductCreateSchema ):
    if auth is None:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="Unauthorized access!")
    product = ProductService.create_product( db, auth, product_req )
    return success( "Product created successfully", product )


# POST    /product/{product_id}/upload_image                  → Upload product images
@router.post( "/{product_id}/upload_image", status_code= status.HTTP_201_CREATED )
async def upload_images ( db: DB_Dependency, auth: Auth_Dependency, product_id: int, files: List[UploadFile] = File(...) ):
    image_paths = []
    if auth is None:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="Unauthorized access!")
    for file in files:
        path = save_product_image( file)
        image_paths.append( path )
    product_img = ProductService.create_product_image( db, product_id, image_paths )
    return success( "Product images uploaded successfully", product_img )


# PUT     /product/{product_id}      → Update product
@router.put( "/{product_id}", status_code = status.HTTP_200_OK )
async def update_product ( db: DB_Dependency, auth: Auth_Dependency, product_id: int, product_req: ProductUpdateSchema ):
    if auth is None:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="Unauthorized access!")
    product = ProductService.update_product( db, auth, product_id, product_req )
    return success( "Product updated successfully", product)


# DELETE  /product/{product_id}      → Delete product
@router.delete( "/{product_id}", status_code = status.HTTP_200_OK )
async def delete_product ( db: DB_Dependency, auth: Auth_Dependency, product_id: int):
    if auth is None:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="Unauthorized access!")
    product = ProductService.delete_product( db, auth, product_id )
    return success( "Product deleted successfully" )


# DELETE  /product/{product_id}/{image_id}      → Delete Product Image
@router.delete("/{product_id}/{image_id}", status_code = status.HTTP_200_OK )
async def delete_product_image ( db: DB_Dependency, auth: Auth_Dependency, product_id: int, image_id: int ):
    if auth is None:
        raise HTTPException ( status_code = status.HTTP_401_UNAUTHORIZED, detail="Unauthorized access!" )
    product = ProductService.delete_product_image( db, product_id, image_id )
    return success( "Product image deleted successfully" )
