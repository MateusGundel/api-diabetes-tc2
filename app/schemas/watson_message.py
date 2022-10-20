from typing import Optional

from pydantic import BaseModel


class Session(BaseModel):
    session: str = None


class MessageInfo(BaseModel):
    type: str
    response: str


class MessageResponse(BaseModel):
    response: MessageInfo

class MessageInput(BaseModel):
    session: str
    message: str
