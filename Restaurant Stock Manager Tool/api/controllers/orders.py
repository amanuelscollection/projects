import random
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import orders as model
from ..models.resource_management import ResourceManagement
from sqlalchemy.exc import SQLAlchemyError
from ..schemas import orders as schema
from ..schemas.order_details import OrderDetailRead, OrderDetailCreate
from typing import List, Optional


def create(db: Session, request: schema.OrderCreate):
    new_order = model.Order(
        customer_phone_number=request.customer_phone_number,
        item_id=request.item_id,
        Amount = request.Amount,
        tracking_number=generate_tracking_number(),
        takeout_delivery=request.takeout_delivery
    )

    try:
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
        
    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not Enough Resources Order was NOT created")

   
    #deduct_resources(db, new_order.id, order_details)

    return new_order

def generate_tracking_number():
    return ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=10))


def read_all(db: Session):
    try:
        result = db.query(model.Order).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request: schema.OrderUpdate):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


def delete(db: Session, item_id):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def calculate_total_price(order_details: List[OrderDetailRead]) -> float:
    total_price = sum(detail.ingredient_amount for detail in order_details)
    return float(total_price)

def deduct_resources(db: Session, order_id: int, order_details: List[schema.OrderDetailCreate]):
    try:
        for detail in order_details:
            if detail.ingredient_amount > 0:
                db.execute(
                    update(ResourceManagement)
                    .where(ResourceManagement.item_id == detail.item_id)
                    .values(ingredient_amount=ResourceManagement.ingredient_amount - 1)
                )
                db.commit()
            
    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

