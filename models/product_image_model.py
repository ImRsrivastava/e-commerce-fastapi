from core.database import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from datetime import datetime

class ProductImageModel (Base):
    __tablename__ = "product_images"

    id          =   Column ( Integer, primary_key = True, index = True )
    product_id  =   Column ( Integer, ForeignKey("products.id") )
    product     =   relationship("ProductModel", back_populates = "images" )

    image_url   =   Column ( String(200), nullable = True )
    create_at   =   Column ( DateTime, default = datetime.utcnow )
    update_at   =   Column ( DateTime, default = datetime.utcnow, onupdate = datetime.utcnow )



