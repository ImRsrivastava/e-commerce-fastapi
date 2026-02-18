from fastapi import HTTPException
from starlette import status
from starlette.status import HTTP_404_NOT_FOUND

from models.shop_model import ShopModel

class ShopService:

    # Shop List
    @staticmethod
    def get_all_shops ( db, auth ):
        shops = db.query(ShopModel).filter(ShopModel.auth_id == auth.id).all()
        return shops

    # Shop Create
    @staticmethod
    def create_shop ( db, auth, shop_req ):
        data = shop_req.dict()
        shop_exists = db.query(ShopModel).filter(ShopModel.email == shop_req.email).first()
        if shop_exists is not None:
            raise HTTPException ( status_code = status.HTTP_409_CONFLICT, detail = "Shop with this email, Already exists!" )
        shop = ShopModel(**data)
        shop.auth_id = auth.id

        db.add(shop)
        db.commit()
        db.refresh(shop)
        return shop

    # Shop Edit
    @staticmethod
    def edit_shop ( db, auth, shop_id ):
        shop = db.query(ShopModel).filter(ShopModel.id == shop_id).filter(ShopModel.auth_id == auth.id).first()
        return shop

    # Shop Update
    @staticmethod
    def update_shop ( db, auth, shop_id, shop_req ):
        shop_exists = db.query(ShopModel).filter(ShopModel.id == shop_id).filter(ShopModel.auth_id == auth.id).first()
        if shop_exists is None:
            return None
        shop = shop_req.dict()
        shop_exists.name = shop['name']
        shop_exists.email = shop['email']
        shop_exists.address = shop['address']
        shop_exists.contact = shop['contact']

        db.add(shop_exists)
        db.commit()
        db.refresh(shop_exists)
        return shop_exists

    # Shop Status Update
    @staticmethod
    def update_shop_status ( db, auth, shop_id, shop_req ):
        shop_exists = db.query(ShopModel).filter(ShopModel.id == shop_id).filter(ShopModel.auth_id == auth.id).first()
        if shop_exists is None:
            return None
        shop = shop_req.dict()
        shop_exists.is_active = shop['is_active']
        db.add(shop_exists)
        db.commit()
        db.refresh(shop_exists)
        return True

    # Shop Delete
    @staticmethod
    def delete_shop ( db, auth, shop_id ):
        shop_exists = db.query(ShopModel).filter(ShopModel.id == shop_id).filter(ShopModel.auth_id == auth.id).first()
        if shop_exists is None:
            return None
        db.delete(shop_exists)
        db.commit()
        return True








