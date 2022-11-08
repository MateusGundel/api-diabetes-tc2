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
    #session_id = "????"
    return {"session": session_id}


@router.post('/message', response_model=list[MessageResponse or None])
async def message(data: MessageInput, db: Session = Depends(deps.get_db)):
    messages_responses = []
    response = WatsonMessage().send_message(data.session, data.message)
    for i in response.get('output').get('generic'):
        log.info(i)
        message_dict = {}
        if i.get('response_type') and i.get('text'):
            message_dict.update({'message': i.get('text'), 'type': 'doris'})
        if i.get('options'):
            options = []
            for option in i.get('options'):
                options.append(option.get('label'))
            if messages_responses[-1]:
                messages_responses[-1].update({'options': options})
        if message_dict:
            messages_responses.append(message_dict)
    log.info(messages_responses)

    return messages_responses
