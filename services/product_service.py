from sqlalchemy.orm import selectinload, load_only
from fastapi import HTTPException
from models.product_model import ProductModel
from models.category_model import CategoriesModel
from models.shop_model import ShopModel
from models.product_image_model import ProductImageModel
from starlette import status
import os


class ProductService:

    # GET ALL PRODUCTS
    @staticmethod
    def get_all_products ( db, auth, name, min_price, max_price, category_id, sort ):
        products = db.query(ProductModel).filter(ProductModel.auth_id == auth.id)
        if name is not None:
            products = products.filter(ProductModel.name.ilike(f"%{name}%"))

        if min_price is not None and max_price is not None:
            products = products.filter(ProductModel.price.between(min_price, max_price))

        if min_price is not None and max_price is None:
            products = products.filter(ProductModel.price >= min_price)

        if min_price is None and max_price is not None:
            products = products.filter(ProductModel.price <= max_price)

        if category_id is not None:
            products = products.filter(ProductModel.category_id == category_id)

        if sort is not None and sort == "price_asc":
            products = products.order_by(ProductModel.price.asc())

        if sort is not None and sort == "price_desc":
            products = products.order_by(ProductModel.price.desc())

        products = products.options(
                    load_only (
                        ProductModel.id,
                        ProductModel.name,
                        ProductModel.description,
                        ProductModel.price,
                        ProductModel.stock,
                        ProductModel.shop_id,
                        ProductModel.category_id
                    ),
                    selectinload(ProductModel.images).load_only(
                        ProductImageModel.id, ProductImageModel.product_id, ProductImageModel.image_url
                    ),
                    selectinload(ProductModel.shop).load_only(ShopModel.id, ShopModel.name),
                    selectinload(ProductModel.category).load_only(CategoriesModel.id, CategoriesModel.name)
            ).all()
        return products


    # GET PRODUCT BY SPECIFIC PRODUCT ID
    @staticmethod
    def get_product_by_id ( db, auth, product_id ):
        product_exist = db.query(ProductModel).filter(ProductModel.id == product_id).filter(ProductModel.auth_id == auth.id).first()
        if product_exist is None:
            raise HTTPException ( status_code= status.HTTP_404_NOT_FOUND, detail= "The product with this ID does not exist." )

        product = db.query(ProductModel)\
                        .filter(ProductModel.id == product_id).filter(ProductModel.auth_id == auth.id)\
                        .options(
                            load_only (
                                ProductModel.id,
                                ProductModel.name,
                                ProductModel.description,
                                ProductModel.price,
                                ProductModel.stock,
                                ProductModel.shop_id,
                                ProductModel.category_id
                            ),
                            selectinload(ProductModel.images).load_only(
                                ProductImageModel.id, ProductImageModel.product_id, ProductImageModel.image_url
                            ),
                            selectinload(ProductModel.shop).load_only(ShopModel.id, ShopModel.name),
                            selectinload(ProductModel.category).load_only(CategoriesModel.id, CategoriesModel.name)
                        ).first()
        return product


    # CREATE PRODUCT
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


    # CREATE PRODUCT IMAGES
    @staticmethod
    def create_product_image ( db, product_id, image_paths: list[str] ):
        images = []
        product_exist = db.query(ProductModel).filter(ProductModel.id == product_id).first()
        if product_exist is None:
            raise HTTPException ( status_code = status.HTTP_404_NOT_FOUND, detail= "The product with this ID does not exist." )

        for path in image_paths:
            img = ProductImageModel(product_id=product_id, image_url=path)
            db.add(img)
            images.append( img )
        db.commit();
        return images


    # UPDATE PRODUCT
    @staticmethod
    def update_product ( db, auth, product_id, product_req ):
        product_exist = db.query(ProductModel).filter(ProductModel.id == product_id).filter(ProductModel.auth_id == auth.id).first()
        if product_exist is None:
            raise HTTPException ( status_code= status.HTTP_404_NOT_FOUND, detail= "The product with this ID does not exist." )

        product = product_req.dict()
        product_exist.shop_id       =   product['shop_id']
        product_exist.category_id   =   product['category_id']
        product_exist.name          =   product['name']
        product_exist.description   =   product['description']
        product_exist.price         =   product['price']
        product_exist.stock         =   product['stock']

        db.add(product_exist)
        db.commit()
        db.refresh(product_exist)
        return product_exist


    # DELETE PRODUCT ALONG WITH ASSOCIATED IMAGES
    @staticmethod
    def delete_product ( db, auth, product_id ):
        product_exist = db.query(ProductModel).filter(ProductModel.id == product_id).filter(ProductModel.auth_id == auth.id).first()
        if product_exist is None:
            raise HTTPException ( status_code= status.HTTP_404_NOT_FOUND, detail= "The product with this ID does not exist." )

        image_exist = db.query(ProductImageModel).filter(ProductImageModel.product_id == product_id).all()
        if image_exist is not None:
            for image in image_exist:
                if image.image_url:
                    file_path = image.image_url

                    # If storing relative path like:
                    # uploads/product/images/abc.jpg
                    if os.path.exists(file_path):
                        os.remove(file_path)

        db.delete(product_exist)
        db.commit()
        return True


    # DELETE PRODUCT IMAGES
    @staticmethod
    def delete_product_image ( db, product_id, image_id):
        image_exist = db.query(ProductImageModel).filter(ProductImageModel.id == image_id).filter(ProductImageModel.product_id == product_id).first()
        if image_exist is None:
            raise HTTPException ( status_code= status.HTTP_404_NOT_FOUND, detail= "The Product Image with this ID does not exist." )

        db.delete(image_exist)
        db.commit()
        return True
