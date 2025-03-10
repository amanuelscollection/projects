from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..models import rewards as model
from sqlalchemy.exc import SQLAlchemyError
from ..schemas import rewards as schema



def create(db: Session, request: schema.RewardsCreate):
    new_reward = model.Rewards(
        phone_number=request.phone_number,
        orders_amount=request.orders_amount,
        discount_amount=request.discount_amount
    )

    try:
        db.add(new_reward)
        db.commit()
        db.refresh(new_reward)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_reward

def read_all(db: Session):
    try:
        rewards = db.query(model.Rewards).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return rewards

def read_one(db: Session, phone_number):
    try:
        reward = db.query(model.Rewards).filter(model.Rewards.phone_number == phone_number).first()
        if not reward:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reward not found")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return reward

def update(db: Session, customer_phone_number):
    customer_orders = db.query(model.Order).filter(model.Order.customer_phone_number == customer_phone_number).count()

    if customer_orders % 5 == 0:
        discount_amount = min(customer_orders // 5 * 5, 50)
    else:
        discount_amount = 0

    rewards = db.query(model.Rewards).filter(model.Rewards.phone_number == customer_phone_number).first()
    if rewards:
        rewards.discount_amount = discount_amount
    else:
        rewards = model.Rewards(phone_number=customer_phone_number, orders_amount=customer_orders, discount_amount=discount_amount)

    try:
        db.add(rewards)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)\

def delete(db: Session, phone_number):
    try:
        reward = db.query(model.Rewards).filter(model.Rewards.phone_number == phone_number).first()
        if not reward:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reward not found")

        db.delete(reward)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return {"message": "Reward deleted successfully"}