from fastapi import HTTPException
from starlette import status
from models.shop_model import ShopModel


class ShopService:

    @staticmethod
    def get_all_shop ( db, auth ):
        if auth is None:
            raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Unauthorized access!")
        shops = db.query(ShopModel).filter(ShopModel.auth_id == auth.id).all()
        return shops