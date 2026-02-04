from sqlachelmy import Column, Integer, String, Float, Boolean, DateTime
from datetime import datetime
from core.database import Base


class Auth (Base):
    __tablename__ = "auths"

    id          =   Column ( Integer, primary_key = True, index = True )
    first_name  =   Column ( String(100), nullable = True )
    last_name   =   Column ( String(100), nullable = True )
    full_name   =   Column ( String(150), nullable = True )
    email       =   Column ( String(150), nullable = True )
    password    =   Column ( String(255), nullable = True )
    is_active   =   Column ( Boolean, default = True )
    created_at  =   Column ( Datetime, default = datetime.utcnow)
    updated_at  =   Column ( Datetime, default = datetime.utcnow, onupdate = datetime.utcnow )