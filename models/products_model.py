from core.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Text, Float
from sqlalchemy.orm import relationship
from datetime import datetime


class ProductModel (Base):
    __tablename__ = "products"

    id          =   Column ( Integer, primary_key = True, index = True )
    shop_id     =   Column ( Integer, ForeignKey("shops.id") )
    shop        =   relationship('ShopModel')

    category_id =   Column ( Integer, ForeignKey("categories.id") )
    category    =   relationship('CategoriesModel')

    auth_id     =   Column ( Integer, ForeignKey("auths.id") )
    auth        =   relationship('AuthModel')

    name        =   Column ( String(150), nullable = True )
    description =   Column ( Text, nullable = True )
    price       =   Column ( Float, nullable = False, default = 0.00 )
    stock       =   Column ( Integer, default = 0, index = True )
    image_url   =   Column ( String(255), nullable = True )
    is_active   =   Column ( Boolean, default = True )
    created_at  =   Column ( DateTime, default = datetime.utcnow )
    updated_at  =   Column ( DateTime, default = datetime.utcnow, onupdate = datetime.utcnow )

