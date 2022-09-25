from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.api import deps
from app.api.deps import get_current_active_user
from app.core.watson import WatsonMessage
from app.schemas import User
from app.schemas.watson_message import SessionId

router = APIRouter()


@router.post('/session', response_model=SessionId)
async def get_session(db: Session = Depends(deps.get_db),
                      current_user: User = Depends(get_current_active_user)
                      ):
    session_id = WatsonMessage().create_session()
    return {"session_id": session_id}


@router.post('/message', response_model=SessionId)
async def message(db: Session = Depends(deps.get_db),
                  current_user: User = Depends(get_current_active_user)
                  ):
    session_id = WatsonMessage().create_session()
    return {"session_id": session_id}
