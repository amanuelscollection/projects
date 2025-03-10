from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import payment_info as model
from ..models import resource_management as resource_model
from sqlalchemy.exc import SQLAlchemyError
from ..schemas import order_details as schema
from api.models.order_details import OrderDetail


def create(db: Session, request: schema.OrderDetailCreate):
    new_order_detail = model.OrderDetail(
        ingredient_name=request.ingredient_name,
        ingredient_amount=request.ingredient_amount,
        item_id=request.item_id
    )

    try:
        db.add(new_order_detail)
        db.commit()
        db.refresh(new_order_detail)
        update_resource_manager(db, new_order_detail)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_order_detail

def update(db: Session, item_id, request: schema.OrderDetailUpdate):
    try:
        order_detail = db.query(model.OrderDetail).filter(model.OrderDetail.id == item_id).first()
        if not order_detail:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order detail not found!")

        update_data = request.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(order_detail, key, value)

        difference = request.ingredient_amount - order_detail.ingredient_amount
        update_resource_manager(db, order_detail.item_id, difference)

        db.commit()
        db.refresh(order_detail)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return order_detail

def update_resource_manager(db: Session, item_id, difference):
    try:
        resource = db.query(resource_model.ResourceManagement).filter(resource_model.ResourceManagement.item_id == item_id).first()
        if not resource:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found!")
        
        resource.ingredient_amount -= difference
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def read_all(db: Session):
    try:
        result = db.query(model.OrderDetail).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        order_detail = db.query(model.OrderDetail).filter(model.OrderDetail.id == item_id).first()
        if not order_detail:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order detail not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return order_detail


def update(db: Session, order_detail, request: schema.OrderDetailUpdate):
    try:
        resource = db.query(resource_model.ResourceManagement).filter(resource_model.ResourceManagement.item_id == order_detail.item_id).first()
        if not resource:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found!")
        
        resource.ingredient_amount -= order_detail.ingredient_amount
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    

def delete(db: Session, item_id):
    try:
        order_detail = db.query(model.OrderDetail).filter(model.OrderDetail.id == item_id)
        if not order_detail.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order detail not found!")
        order_detail.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
