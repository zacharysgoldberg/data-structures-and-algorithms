from fastapi import FastAPI, Depends
from api.models import Users, Orders, Base
from api.database import engine, db
from api.routers import auth, orders
from api.routers.auth import hash_password
from sqlalchemy.orm import Session
# from pydantic import BaseModel

app = FastAPI()

# class CreateUser(BaseModel):
#     username: str
#     password: str

Base.metadata.create_all(bind=engine)


@app.get("/")
async def index(db: Session = Depends(db)):
    user = db.query(Users).filter(Users.username == "ExampleUser").first()
    # [If user does not exist create user and sample records for testing api]
    if user is None:
        users_model = Users()
        users_model.username = "ExampleUser"
        hashed_password = hash_password("test1234!")
        users_model.password = hashed_password
        db.add(users_model)

        db.commit()

        orders_model1 = Orders()
        orders_model1.order_time = "2022-08-11 12:15:00"
        orders_model1.address = "6868 Capri Ave, Ventura CA"
        db.add(orders_model1)

        orders_model2 = Orders()
        orders_model2.order_time = "2022-08-11 13:15:00"
        orders_model2.address = "311 E Daily Dr, Camarillo CA"
        db.add(orders_model2)

        orders_model3 = Orders()
        orders_model3.order_time = "2022-08-11 14:15:00"
        orders_model3.address = "3900 Bluefin Cir, Oxnard CA"
        db.add(orders_model3)

        orders_model4 = Orders()
        orders_model4.order_time = "2022-08-11 15:15:00"
        orders_model4.address = "2701 Saviers Rd, Oxnard CA"
        db.add(orders_model4)

        orders_model5 = Orders()
        orders_model5.order_time = "2022-08-11 16:15:00"
        orders_model5.address = "4667 Telegraph Rd, Ventura CA"
        db.add(orders_model5)

        db.commit()

        return "Pizza Drone Created"

    return "Pizza Drone Ready..."

# [Connecting routers]
app.include_router(auth.router)
app.include_router(orders.router)
