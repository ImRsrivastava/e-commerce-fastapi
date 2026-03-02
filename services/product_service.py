from fastapi import HTTPException
from models.product_model import ProductModel
from models.category_model import CategoriesModel
from models.shop_model import ShopModel
from models.product_image_model import ProductImageModel
from starlette import status


class ProductService:

    @staticmethod
    def get_all_products ( db, auth ):
        products = db.query(ProductModel).filter(ProductModel.auth_id == auth.id).all()
        return products

    @staticmethod
    def create_product ( db, auth, product_req ):
        data = product_req.dict()
        shop_exists = db.query(ShopModel).filter(ShopModel.id == data['shop_id']).first()
        category_exists = db.query(CategoriesModel).filter(CategoriesModel.id == data['category_id']).first()
        data_exists = db.query(ProductModel)\
                                    .filter(ProductModel.shop_id == data['shop_id'])\
                                    .filter(ProductModel.category_id == data['category_id'])\
                                    .filter(ProductModel.name == data['name']) .first()
        if shop_exists is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "The shop with this ID does not exist." )

        if category_exists is None:
            raise HTTPException ( status_code = status.HTTP_404_NOT_FOUND, detail= "The category with this ID does not exist." )

        if data_exists is not None:
            raise HTTPException ( status_code = status.HTTP_409_CONFLICT, detail= "The product with this name, already exists.")

        product = ProductModel(**data)
        product.auth_id = auth.id
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    @staticmethod

