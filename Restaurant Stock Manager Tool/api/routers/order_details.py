from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..controllers import order_details as controller
from ..schemas.order_details import OrderDetailRead, OrderDetailCreate, OrderDetailUpdate
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Order Details'],
    prefix="/orderdetails"
)

@router.post("/", response_model=OrderDetailRead)
def create_order_detail(request: OrderDetailCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.put("/{item_id}", response_model=OrderDetailRead)
def update_order_detail(item_id: int, request: OrderDetailUpdate, db: Session = Depends(get_db)):
    return controller.update(db, item_id, request)

@router.get("/", response_model=List[OrderDetailRead])
def read_all_order_details(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{item_id}", response_model=OrderDetailRead)
def read_order_detail(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id)

@router.delete("/{item_id}", status_code=204)
def delete_order_detail(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, item_id)
