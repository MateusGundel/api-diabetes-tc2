import logging

from fastapi import Depends, APIRouter

from app.api import deps
from app.core.watson import WatsonMessage
from app.schemas.watson_message import Session, MessageResponse, MessageInput

log = logging.getLogger(__name__)

router = APIRouter()


@router.get('/session', response_model=Session)
async def get_session(db: Session = Depends(deps.get_db)):
    session_id = WatsonMessage().create_session()
    return {"session": session_id}


@router.post('/message', response_model=list[MessageResponse])
async def message(data: MessageInput, db: Session = Depends(deps.get_db)):
    response = WatsonMessage().send_message(data.session, data.message)
    log.info(response)
    messages = []

    for i in response.get('output').get('generic'):
        if i.get('response_type') and i.get('text'):
            detail = {"type": "text", "response": i.get('text')}
            messages.append({"response": detail})
        if i.get('options'):
            for option in i.get('options'):
                detail = {"type": "text", "response": option.get('label')}
                messages.append({"response": detail})

    log.info(messages)
    return messages
