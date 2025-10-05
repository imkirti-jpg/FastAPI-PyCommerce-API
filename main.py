from Routers import products , catergories , users , auth , carts ,accounts
from fastapi import FastAPI
from database import Base, engine


app = FastAPI()


app.include_router(products.routers)
app.include_router(catergories.routers)
app.include_router(users.routers)
app.include_router(auth.routers)
app.include_router(carts.routers)
app.include_router(accounts.routers)