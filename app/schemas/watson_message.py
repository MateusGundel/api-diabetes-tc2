from typing import Optional

from pydantic import BaseModel


class Session(BaseModel):
    session: str = None


class MessageInfo(BaseModel):
    type: str
    response: str


class MessageResponse(BaseModel):
    message: str
    type: str
    options: list = None


class MessageInput(BaseModel):
    session: str
    message: str
