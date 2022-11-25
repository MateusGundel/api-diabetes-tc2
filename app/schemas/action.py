from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ActionBase(BaseModel):
    user_hash: str = None
    value: str = None
    type: str = None


class CreateAction(ActionBase):
    user_hash: str
    value: str
    type: str


class UpdateAction(ActionBase):
    user_hash: str
    value: str
    type: str


class Action(ActionBase):
    id: int
    data: datetime

    class Config:
        orm_mode = True
