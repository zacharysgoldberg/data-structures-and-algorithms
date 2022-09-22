from fastapi import APIRouter, Request, Depends
from .auth import get_current_user
from ..database import db
from sqlalchemy.orm import Session
from ..models import Orders
import requests
from ..commands.gps import get_coords_by_address, TSP
import csv
import pandas as pd


router = APIRouter(
    prefix="/orders",
    tags=["orders"],
    responses={401: {"order": "Not found"}}
)

# [Request to optimize path for orders/addresses]


@router.get('/optimize-path')
async def sort_order(db: Session = Depends(db)):
    # [For CSV]
    with open("api/routers/orders.csv", "r") as file:
        reader = csv.DictReader(file)
        # header = next(reader)
        addresses = [row['address'] for row in reader]
        
    # [For postgres]
    # addresses = db.query(Orders.address).all()

    coords_list = [get_coords_by_address(order) for order in addresses]
    optimal_path_coords, orders = TSP(coords_list)

    order_of_path = [int(order) for order in orders]
    print(order_of_path)

    data = {"coords": optimal_path_coords, "orders": order_of_path}

    return data

# [Request to get the next order upon successful authorization]


@router.get('/get-next-order/{order_id}')
async def get_next_order(request: Request, order_id: int, db: Session = Depends(db)):
    user = await get_current_user(request)
    if user is None:
        response = requests.post("http://localhost:8000/auth/token",
                                 data={"username": "ExampleUser", "password": "test1234!"})
        print(response.text)

    # [Returning next order based on order id]
    next_order = db.query(Orders.address).filter(Orders.id == order_id).first()
    if next_order:
        print(next_order)
        return next_order

    return False

# [To update order delivery to True]


@router.post('/deliver-order/{order_id}')
async def deliver_order(request: Request, order_id: int, db: Session = Depends(db)):
    user = await get_current_user(request)
    if user is None:
        response = request.post("http://localhost:8000/auth/token",
                                data={"username": "ExampleUser", "password": "test1234!"})
        print(response.text)
    
    # [For postgres]
    # order_model = db.query(Orders).filter(Orders.id == order_id).first()
    # order_model.delivered = True
    # db.add(order_model)
    # db.commit()
    return True
