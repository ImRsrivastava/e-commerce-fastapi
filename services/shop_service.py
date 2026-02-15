from fastapi import HTTPException
from starlette import status
from models.shop_model import ShopModel


class ShopService:

    @staticmethod
    def get_all_shop ( db, auth ):
        if auth is None:
            raise HTTPException( status_code = status.HTTP_401_UNAUTHORIZED, detail = "Unauthorized access!" )
        shops = db.query(ShopModel).filter(ShopModel.auth_id == auth.id).all()
        return shops

    @staticmethod
    def create_shop ( db, auth, shop_req ):
        data = shop_req.dict()
        if auth is None:
            raise HTTPException( status_code = status.HTTP_401_UNAUTHORIZED, detail = "Unauthorized access!" )
        shop_exists = db.query(ShopModel).filter(ShopModel.email == shop_req.email).first()

        if shop_exists is not None:
            raise HTTPException ( status_code = status.HTTP_409_CONFLICT, detail = "Shop with this email, Already exists!" )

        shop = ShopModel(**data)
        shop.auth_id = auth.id

        db.add(shop)
        db.commit()
        db.refresh(shop)
        return shop

