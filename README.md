# E-Commerce FastAPI Backend
This project is a modular backend system built using FastAPI, designed to simulate a real-world e-commerce service. It follows clean architecture principles with separation of concerns across routes, schemas, services, models, core configuration, and utility helpers. The goal of this project is to provide a production-ready API structure suitable for learning, resume showcase, and future expansion.


# Module Wise Overview
1. Authentication Module
Handles user registration and login functionality using JWT-based authentication. Includes secure password hashing, token generation, and token verification. Ensures users can safely access protected routes without using RBAC at this stage.

2. User Management Module
Manages basic user information such as name, email, hashed passwords, and activation status. Enforces unique email constraints and integrates with the authentication system. Exposes endpoints for retrieving the logged-in user profile.

3. Product Management Module
Supports full CRUD operations for products including creation, listing, updating, and deletion. Each product includes fields such as name, description, price, stock, category mapping, timestamps, and active status. Also supports image upload functionality for product media storage.

4. Category Management Module
Provides API endpoints to create, update, delete, and list product categories. Acts as a parent grouping mechanism for organizing products. Useful for filtering and structuring the product catalog.

5. Shop Management Module
Supports full CRUD operations for shops including creation, listing, updating, and deletion. Each shop includes fields such as name, description, address, contact details, timestamps, and active status. Acts as a parent grouping mechanism for organizing products under specific shops.

6. Core Module
Contains core application logic shared across the project:
   - Database configuration and session handling using SQLAlchemy
   - Environment-based configuration loading
   - Security utilities including password hashing and JWT helpers
This module ensures centralized management of critical project resources.

7. Services Module
Implements the business logic for users, products, and categories. Service classes interact with the database and perform validations before returning data to the routes layer. This separation enhances maintainability and makes the code easier to test.

8. Schemas Module
Includes Pydantic models used for request validation and response serialization. Each module (users, products, categories) has its own set of schemas to enforce strict API payload structures.

9. Models Module
Contains SQLAlchemy ORM models that define the database tables. Each model maps to a table with proper relationships, constraints, indexing, and timestamps.

10. Routes Module
Defines public API endpoints for the application. Routes are modularized per feature, making the API easier to scale, maintain, and version in the future.

11. Utils Module
Provides reusable helper utilities such as image handling, pagination helpers, and custom response formatting. These utilities keep the main business logic clean and organized.


# API Endpoints Overview
Authentication Endpoints:
   - POST /users/register : Register a new user.
   - POST /users/login : Generate JWT token for authentication.
   - GET /users/me : Retrieve the authenticated user profile.

Product Endpoints:
   - GET /products : List all products (supports search, filter, pagination).
   - GET /products/{id} : Retrieve product by ID.
   - POST /products : Create a new product.
   - PUT /products/{id} : Update an existing product.
   - DELETE /products/{id} : Soft delete a product.
   - POST /products/{id}/upload-image : Upload product image.

Category Endpoints:
   - GET /categories : List all categories.
   - POST /categories : Create a category.
   - PUT /categories/{id} : Update category information.
   - DELETE /categories/{id} : Remove a category.

Shop Endpoints:
   - GET /shops : List all shops.
   - POST /shops : Create a shop.
   - PUT /shops/{id} : Update shop information.
   - DELETE /shops/{id} : Remove a shop.

This API follows a clean and modular approach with separated layers for routes, services, schemas, and database models. All endpoints return structured responses and use Pydantic-based validation to enforce payload integrity.


# PROJECT SUMMARY
This project is a modular FastAPI backend designed to simulate a real e-commerce system. It includes user authentication, product and category  management, image uploads, and strict data validation using Pydantic. SQLAlchemy ORM is used for database modeling, with clean service-layer logic for scalability. The project follows production-style practices, making it ideal for learning FastAPI, understanding backend architecture, and showcasing on a resume or GitHub portfolio.


# AUTHOR
Im@Rsrivastava
Backend Engineer


