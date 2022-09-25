import logging
from typing import Optional

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import AssistantV2
from ibm_watson.assistant_v2 import MessageInput
from requests import Response

from app.core.config import Settings

log = logging.getLogger(__name__)


class WatsonMessage:
    assistant: AssistantV2 = None
    assistant_id: str = None

    def __init__(self) -> None:
        authenticator = IAMAuthenticator(apikey=Settings.WATSON_API_KEY)
        self.assistant = AssistantV2(version=Settings.WATSON_VERSION, authenticator=authenticator)
        self.assistant_id = Settings.WATSON_ASSISTANT_ID

    def create_session(self) -> Optional[str, None]:
        try:
            response = self.assistant.create_session(assistant_id=self.assistant_id).get_result()
            return response.get('session_id')
        except Exception as e:
            log.error(f"Erro ao criar sessão pasa o assistant_id {self.assistant_id} - {e}")
        return None

    def delete_session(self, session_id: str) -> None:
        try:
            self.assistant.delete_session(assistant_id=self.assistant_id,
                                          session_id=session_id).get_result()
            log.info(f"Sucesso ao remover a sessão {session_id}")
        except Exception as e:
            log.error(f"Erro ao excluir sessão {session_id} - {e}")

    def send_message(self, session_id: str, text: str) -> Response:
        message_input = MessageInput(message_type='text', text=text)
        return self.assistant.message(
            assistant_id=self.assistant_id,
            session_id=session_id,
            input=message_input).get_result()
