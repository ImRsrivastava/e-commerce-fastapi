from fastapi import HTTPException, Depends
from typing import Annotated
from starlette import status
from models.auth_model import AuthModel
from core.security import oauth2Beare, verify_access_token
from sqlalchemy.orm import Session
from core.database import get_db


class CommonService:

    @staticmethod
    def get_auth_user ( db: Annotated[ Session, Depends(get_db)], token: Annotated[str, Depends(oauth2Beare)] ):
        payload = verify_access_token( token )
        auth_id = payload.get('auth_id')
        auth_email = payload.get('email')

        if auth_id is None or auth_email is None:
            raise HTTPException ( status_code = status.HTTP_401_UNAUTHORIZED )

        auth = db.query(AuthModel).filter(AuthModel.id == auth_id).first()
        return auth

# ADD THIS AFTER THE CLASS
Auth_Dependency = Annotated[ AuthModel, Depends(CommonService.get_auth_user) ]
