from fastapi import FastAPI
from core.database import engine, Base
from models import auth_model, categories_model, shop_model, products_model


Base.metadata.create_all ( bind = engine )
app = FastAPI(title="E-Commerce Product API")

