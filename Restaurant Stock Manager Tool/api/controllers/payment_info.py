from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import payment_info as model
from sqlalchemy.exc import SQLAlchemyError
from ..schemas import payment_info as schema
from sqlalchemy import text

def create ( db: Session, request: schema.PaymentInfoCreate):
    new_item = model.PaymentInfo(
        card_info=request.card_info,
        payment_type=request.payment_type,
        order_id=request.order_id
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item

def read_all(db: Session):
    try:
        result = db.query(model.PaymentInfo).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result

def read_one(db: Session, item_id):
    try:
        item = db.query(model.PaymentInfo).filter(model.PaymentInfo.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item

def update_payment_info(db: Session, order_id: int, request: schema.PaymentInfoUpdate):
    try:
        
        price_query = text(f"SELECT price FROM order_details WHERE order_id = {order_id}")
        price = db.execute(price_query).scalar()

        
        if price is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Price not found for the provided order_id")

        
        payment_info = db.query(model.PaymentInfo).filter(model.PaymentInfo.order_id == order_id).first()
        if not payment_info:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment info not found for the provided order_id")

        payment_info.card_info = request.card_info
        payment_info.payment_type = request.payment_type

        
        payment_info.total_price = price

        
        db.commit()
        db.refresh(payment_info)

        return payment_info
    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def delete(db: Session, item_id):
    try:
        item = db.query(model.Menu).filter(model.PaymentInfo.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


