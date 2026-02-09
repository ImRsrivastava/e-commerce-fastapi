from fastapi import APIRouter, HTTPException
from starlette import status
from core.database import DB_Dependency
from services.common_service import Auth_Dependency
from services.category_service import CategoriesService
from utils.response import success
from schemas.category_schema import CategoryCreateSchema, CategoryUpdateSchema


router = APIRouter(
    prefix = '/category',
    tags = ["Category-Routes"]
)

# GET ALL CATEGORIES LIST
@router.get( "/", status_code = status.HTTP_200_OK )
async def get_all_categories ( db: DB_Dependency, auth: Auth_Dependency ):
    categories = CategoriesService.get_categories( db, auth )
    if not categories:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Category not found.")
    return success( "All categories retrieved successfully.", categories )

# GET CATEGORIES BY CATEGORY NAME
@router.get( "/{category_name}", status_code = status.HTTP_200_OK )
async def get_category_by_name ( db: DB_Dependency, auth: Auth_Dependency, category_name: str ):
    category = CategoriesService.get_category_by_name( db, auth, category_name )
    if not category:
        raise HTTPException ( status_code = status.HTTP_404_NOT_FOUND, detail = "Category not found." )
    return success( "Category successfully fetched using the name", category )

# CREATE NEW CATEGORY
@router.post( "/",  status_code = status.HTTP_201_CREATED )
async def create_category ( db: DB_Dependency, auth: Auth_Dependency, category_req: CategoryCreateSchema ):
    category = CategoriesService.create_category( db, auth, category_req )
    return success( "Category created successfully", category )

# UPDATE CATEGORY INFORMATION
@router.put('/{category_id}', status_code = status.HTTP_204_NO_CONTENT )
async def update_category ( db: DB_Dependency, auth: Auth_Dependency, category_id: int, category_req: CategoryUpdateSchema ):
    category = CategoriesService.update_category( db, auth, category_id, category_req )
    return success( "Category updated successfully", category )

# DELETE CATEGORY INFORMATION
@router.delete('/{category_id}', status_code = status.HTTP_204_NO_CONTENT )
async def delete_category ( db: DB_Dependency, auth: Auth_Dependency, category_id: int ):
    category = CategoriesService.delete_category( db, auth, category_id)
    return success( "Category deleted successfully", True )














































