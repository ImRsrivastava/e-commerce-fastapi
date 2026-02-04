from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from core.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime


class ShopModel (Base):
    __tablename__ = 'shops'

    id          =   Column ( Integer, primary_key = True, index = True )

    auth_id     =   Column ( Integer, ForeignKey("auths.id") )
    auth        =   relationship('AuthModel')

    name        =   Column ( String(150), nullable = True )
    email       =   Column ( String(150), nullable = True, unique = True )
    address     =   Column ( String(200), nullable = True )
    contact     =   Column ( String(50), nullable = True )

    is_active   =   Column ( Boolean, default = True )
    created_at  =   Column ( DateTime, default = datetime.utcnow )
    updated_at  =   Column ( DateTime, default = datetime.utcnow, onupdate = datetime.utcnow )