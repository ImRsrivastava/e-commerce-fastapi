from models.category_model import CategoriesModel
from fastapi import HTTPException
from starlette import status

class CategoriesService:

    @staticmethod
    def get_categories ( db, auth ):
        if auth is None:
            raise HTTPException( status_code = status.HTTP_401_UNAUTHORIZED, detail = "Unauthorized access!" )
        categories = db.query(CategoriesModel).filter(CategoriesModel.created_by == auth.id).all()
        return categories

    @staticmethod
    def get_category_by_name ( db, auth, category_name ):
        if auth is None:
            raise HTTPException( status_code = status.HTTP_401_UNAUTHORIZED, detail = "Unauthorized access!" )
        category = db.query(CategoriesModel).filter( CategoriesModel.name.ilike(f"%{category_name}%") ).first()
        return category

    @staticmethod
    def create_category ( db, auth, category_req ):
        data = category_req.dict()
        if auth is None:
            raise HTTPException( status_code = status.HTTP_401_UNAUTHORIZED, detail = "Unauthorized access!" )

        if db.query(CategoriesModel).filter(CategoriesModel.name == category_req.name).first():
            raise HTTPException( status_code = status.HTTP_409_CONFLICT, detail = "Category with this name, already exists" )

        category = CategoriesModel(**data)
        category.created_by = auth.id

        db.add(category)
        db.commit()
        db.refresh(category)
        return category

    @staticmethod
    def update_category ( db, auth, category_id, category_req ):
        if auth is None:
            raise HTTPException( status_code = status.HTTP_401_UNAUTHORIZED, detail = "Unauthorized access!" )
        category = db.query(CategoriesModel).filter(CategoriesModel.id == category_id).filter(CategoriesModel.created_by == auth.id).first()
        if category is None:
            raise HTTPException( status_code = status.HTTP_404_NOT_FOUND, detail = "Category not found!" )
        cate = category_req.dict()
        category.name = cate['name']
        category.description = cate['description']

        db.add(category)
        db.commit()
        db.refresh(category)
        return category

    @staticmethod
    def delete_category ( db, auth, category_id ):
        if auth is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail = "Unauthorized access!")
        category = db.query(CategoriesModel).filter(CategoriesModel.id == category_id).filter(
            CategoriesModel.created_by == auth.id).first()
        if category is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Category not found!")
        db.delete(category)
        db.commit()
        return True
