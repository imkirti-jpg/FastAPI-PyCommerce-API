E-commerce Backend API

Built with Python & FastAPI for High-Performance Applications

📋 Overview

This project is a robust backend API designed to power a modern, scalable e-commerce platform. Built using FastAPI and Python, it leverages asynchronous programming for speed and efficiency, allowing it to handle high volumes of concurrent requests typical of busy online stores.

The API covers all core e-commerce functionality, including product management, user authentication, secure account handling, and end-to-end shopping cart operations. It fully adheres to the OpenAPI 3.0 specification, providing interactive documentation via /docs and a machine-readable contract for seamless frontend integration.

✨ Features
📦 Product & Catalog Management

Products: Full CRUD operations for managing product listings, pricing, stock, descriptions, and metadata.

Categories: CRUD operations for organizing products, enabling easy browsing, search, and filtering.

👤 User & Authentication

Authentication: Secure, stateless JWT-based system with endpoints for signup, login, and token refresh.

Users: Administrative endpoints for retrieving and managing users.

Accounts: Sensitive endpoints for users to access and update their personal information, including profile updates and account deactivation.

🛒 Shopping Cart

Create, view, update, and delete shopping carts.

Manage cart items (add, remove, update quantities).

Clear cart upon order submission or cancellation, ensuring accurate purchase flow.

🛠️ Technology Stack

Framework: FastAPI

Language: Python 3.11+

Data Validation: Pydantic

Database: SQLite (development) — designed to be DB-agnostic for PostgreSQL or MongoDB in production

Dependency Management: pip / Poetry

🚀 Setup & Installation

Clone the repository

git clone [YOUR_REPO_URL]
cd [project-name]


Create and activate a virtual environment

python -m venv venv
source venv/bin/activate  # macOS/Linux
# Windows: .\venv\Scripts\activate


Install dependencies

pip install -r requirements.txt
# OR
poetry install


Configure environment variables
Create a .env file in the root directory:

DATABASE_URL="sqlite:///./sql_app.db"  # Update for production
SECRET_KEY="your-super-secret-key-for-jwt"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30


Run the server

uvicorn main:app --reload


Server will be accessible at http://127.0.0.1:8000
.

📖 API Documentation

Interactive Swagger UI is available at:

http://127.0.0.1:8000/docs

Test all API routes, inspect request/response schemas, and explore security mechanisms directly in the browser.

📸 Screenshots
