from fastapi import FastAPI, Request
from core.database import engine, Base
from models import auth_model, category_model, shop_model, product_model
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from routes import auth_route, category_route


Base.metadata.create_all ( bind = engine )
app = FastAPI(title="E-Commerce Product API")

# -------------------------------
# 🟦 GLOBAL EXCEPTION HANDLERS
# -------------------------------
# 1️⃣ Handle Integrity Errors (Duplicate, FK errors, constraints)
@app.exception_handler(IntegrityError)
async def integrity_error_handler(request: Request, exc: IntegrityError) -> JSONResponse:
    return JSONResponse(
        status_code = exc.code,
        content = {
            "status": exc.code,
            "message": "Database integrity error (duplicate or invalid data).",
            "details": str(exc.orig)
        }
    )

# 2️⃣ Handle Generic SQLAlchemy Errors
@app.exception_handler(SQLAlchemyError)
async def sqlalchemy_error_handler(request: Request, exc: SQLAlchemyError) -> JSONResponse:
    return JSONResponse (
        status_code = exc.code,
        content = {
            "status": exc.code,
            "message": "Database operation failed.",
            "details": str(exc)
        }
    )

# 3️⃣ Handle ALL OTHER Python Exceptions
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    return JSONResponse(
        status_code = exc.code,
        content = {
            "status": exc.code,
            "message": "Internal server error.",
            "details": str(exc)
        }
    )

# -------------------------------
# 🟦 ROUTES
# -------------------------------
app.include_router( auth_route.router )
app.include_router( category_route.router )