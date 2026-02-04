from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from core.database import Base


class CategoriesModel (Base):
    __tablename__ = "categories"

    id          =   Column ( Integer, primary_key = True, index = True )
    name        =   Column ( String(150), nullable = True )
    description =   Column ( String(200), nullable = True )

    created_by  =   Column ( Integer, ForeignKey('auths.id') )
    auth        =   relationship('AuthModel')

    is_active   =   Column ( Boolean, default = True )
    created_at  =   Column ( DateTime, default = datetime.utcnow )
    updated_at  =   Column ( DateTime, default = datetime.utcnow, onupdate = datetime.utcnow )

