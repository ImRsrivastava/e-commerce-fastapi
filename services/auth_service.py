from fastapi import HTTPException
from models.auth_model import AuthModel
from sqlalchemy.exc import IntegrityError
from core.security import hash_password, verify_password, create_access_token


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
    def login_service ( db, email, password ):
        try:
            auth = db.query(AuthModel).filter(AuthModel.email == email).first()
            if not auth:
                raise HTTPException (
                    status_code = 400,
                    detail = "Invalid credentials!"
                )
            if not verify_password (password, auth.password):
                raise HTTPException (
                    status_code = 400,
                    detail = "Invalid email or password!"
                )
            auth_token = create_access_token ({ "sub": str(auth.id), "auth_id": auth.id, "email": auth.email })
            return auth_token
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

