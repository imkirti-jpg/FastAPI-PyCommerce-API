# FastAPI E-Commerce API

A RESTful API for an e-commerce application built with FastAPI, providing endpoints for product management, user authentication, shopping carts, and more.

## Features

- **Product Management**: Full CRUD operations for products
- **Category Management**: Organize products into categories
- **User Management**: User registration and profile management
- **Authentication**: Secure user signup, login, and token refresh
- **Shopping Cart**: Cart functionality for users
- **Account Management**: User profile and account operations

## API Endpoints

### Products
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/products/` | Get all products |
| `POST` | `/products/` | Create a new product |
| `GET` | `/products/{product_id}` | Get specific product |
| `PUT` | `/products/{product_id}` | Update product |
| `DELETE` | `/products/{product_id}` | Delete product |

### Categories
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/catergories/` | Get all categories |
| `POST` | `/catergories/` | Create a new category |
| `GET` | `/catergories/{category_id}` | Get specific category |
| `PUT` | `/catergories/{category_id}` | Update category |
| `DELETE` | `/catergories/{category_id}` | Delete category |

### Users
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/users/` | Get all users |
| `POST` | `/users/` | Create a new user |
| `GET` | `/users/{user_id}` | Get specific user |
| `PUT` | `/users/{user_id}` | Update user |
| `DELETE` | `/users/{user_id}` | Delete user |

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/auth/signup` | User registration |
| `POST` | `/auth/login` | User login |
| `POST` | `/auth/refresh-token` | Refresh authentication token |

### Shopping Carts
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/carts/{cart_id}` | Get cart details |
| `PUT` | `/carts/{cart_id}` | Update cart |
| `DELETE` | `/carts/{cart_id}` | Delete cart |
| `POST` | `/carts/` | Create new cart |

### Account Management
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/accounts/me` | Get current user info |
| `PUT` | `/accounts/me` | Edit current user info |
| `DELETE` | `/accounts/me` | Delete current user account |

## Installation

1. **Clone the repository:**
```bash
git clone <repository-url>
cd <project-directory>
```

### 1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 1. Install dependencies:

```bash
pip install -r requirements.txt
```

### 2. Run the application:

```bash
uvicorn main:app --reload
```

## Usage

The API will be available at http://localhost:8000

· Interactive API documentation: http://localhost:8000/docs
· Alternative documentation: http://localhost:8000/redoc

## Screenshots





## Requirements

The project requires the following dependencies (add to requirements.txt):

```txt
fastapi==0.104.1
uvicorn==0.24.0
python-multipart==0.0.6
python-jose==3.3.0
passlib==1.7.4
```

License

This project is licensed under the MIT License.

