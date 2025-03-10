from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..schemas import RewardsCreate, RewardsRead, RewardsUpdate
from ..controllers import rewards
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Rewards'],
    prefix="/rewards"
)

@router.post("/rewards/", response_model=RewardsRead)
def create_reward(reward: RewardsCreate, db: Session = Depends(get_db)):
    return rewards.create(db, reward)

@router.get("/rewards/", response_model=List[RewardsRead])
def read_rewards(db: Session = Depends(get_db)):
    return rewards.read_all(db)

@router.get("/rewards/{phone_number}", response_model=RewardsRead)
def read_reward(phone_number: str, db: Session = Depends(get_db)):
    return rewards.read_one(db, phone_number)

@router.put("/rewards/{phone_number}")
def update_reward(phone_number: str, db: Session = Depends(get_db)):
    return rewards.update(db, phone_number)

@router.delete("/rewards/{phone_number}")
def delete_reward(phone_number: str, db: Session = Depends(get_db)):
    return rewards.delete(db, phone_number)