from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class RewardsBase(BaseModel):
    reward_name: str
    reward_description: str
    reward_points: int

class RewardsCreate(RewardsBase):
    pass

class RewardsRead(RewardsBase):
    id: int

    class Config:
        orm_mode = True

class RewardsUpdate(RewardsBase):
    pass