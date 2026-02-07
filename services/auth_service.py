from fastapi import HTTPException
from models.auth_model import AuthModel
from sqlalchemy.exc import IntegrityError
from core.security import hash_password


class AuthService:

    @staticmethod
    def register_service ( db, auth_user ):
        try:
            data = auth_user.dict()
            data['password'] = hash_password(data['password'])
            auth = AuthModel(**data)

            db.add(auth)
            db.commit()
            db.refresh(auth)
            return auth
        except IntegrityError as ie:
            db.rollback()
            raise HTTPException (
                status_code = 400,
                detail = str(ie.orig)
            )
        except Exception as ex:
            db.rollback()
            raise HTTPException (
                status_code = 500,
                detail = str(ex.orig)
            )

    @staticmethod
    def login_service ( db, auth_user ):
        try:
            return True
        except IntegrityError as ie:
            db.rollback()
            raise HTTPException(
                status_code=400,
                detail=str(ie.orig)
            )
        except Exception as ex:
            db.rollback()
            raise HTTPException(
                status_code=500,
                detail=str(ex.orig)
            )