from app.crud.base import CRUDBase
from app.models.action import Action
from app.schemas.action import CreateAction, UpdateAction


class CRUDAction(CRUDBase[Action, CreateAction, UpdateAction]):
    def __int__(self):
        super().__init__()


action = CRUDAction(Action)
