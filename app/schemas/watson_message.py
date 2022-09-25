from typing import Optional

from pydantic import BaseModel


class SessionId(BaseModel):
    session_id: Optional[str] = None
