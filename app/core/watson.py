import logging
from typing import Optional

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import AssistantV2, TextToSpeechV1
from ibm_watson.assistant_v2 import MessageInput
from requests import Response

from app.core.config import Settings

log = logging.getLogger(__name__)


class WatsonMessage:
    assistant: AssistantV2 = None
    assistant_id: str = None

    def __init__(self) -> None:
        settings = Settings()
        log.info(f"watsion api key {settings.WATSON_API_KEY}")
        log.info(f"watsion version {settings.WATSON_VERSION}")
        log.info(f"watsion assistant ID {settings.WATSON_ASSISTANT_ID}")
        authenticator = IAMAuthenticator(apikey=settings.WATSON_API_KEY)
        self.assistant = AssistantV2(version=settings.WATSON_VERSION, authenticator=authenticator)
        self.assistant.set_service_url('https://api.au-syd.assistant.watson.cloud.ibm.com')
        self.assistant.set_disable_ssl_verification(True)
        self.assistant_id = settings.WATSON_ASSISTANT_ID

    def create_session(self) -> str:
        try:
            response = self.assistant.create_session(assistant_id=self.assistant_id).get_result()
            return response.get('session_id')
        except Exception as e:
            log.error(f"Erro ao criar sessão para o assistant_id {self.assistant_id} - {e}")
        return ""

    def delete_session(self, session_id: str) -> None:
        try:
            self.assistant.delete_session(assistant_id=self.assistant_id,
                                          session_id=session_id).get_result()
            log.info(f"Sucesso ao remover a sessão {session_id}")
        except Exception as e:
            log.error(f"Erro ao excluir sessão {session_id} - {e}")

    def send_message(self, session_id: str, text: str) -> Response:
        """
        TEstes :????
        """
        log.info(session_id)
        log.info(text)
        message_input = MessageInput(message_type='text', text=text)
        return self.assistant.message(
            assistant_id=self.assistant_id,
            session_id=session_id,
            input=message_input).get_result()


class WatsonTextToSpeech:
    text_to_speech = None
    voice = 'pt-BR_IsabelaV3Voice'

    def __init__(self) -> None:
        settings = Settings()
        authenticator = IAMAuthenticator(settings.TEXT_SPEECH_API_KEY)
        self.text_to_speech = TextToSpeechV1(
            authenticator=authenticator
        )
        self.text_to_speech.set_service_url(settings.TEXT_SPEECH_URL)
        self.text_to_speech.set_disable_ssl_verification(True)

    def get_audio(self, text):
        audio = self.text_to_speech.synthesize(
            text,
            voice=self.voice,
            accept='audio/wav'
        ).get_result().content
        return audio
