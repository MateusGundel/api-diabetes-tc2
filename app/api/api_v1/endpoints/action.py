import logging

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.api import deps
from app import crud
from app.schemas.action import ActionBase, Action

router = APIRouter()

log = logging.getLogger(__name__)


@router.post('/', response_model=Action)
async def alguma_coisa(action_obj: ActionBase, db: Session = Depends(deps.get_db)):
    act = crud.action.create(db, obj_in=action_obj)
    return act
