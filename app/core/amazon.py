import logging
import wave
from io import BytesIO

from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError

log = logging.getLogger(__name__)


class PollySpeech:
    auido_channels = 1  # Polly's output is a mono audio stream
    rate = 16000  # Polly supports 16000Hz and 8000Hz output for PCM format
    audio_sample_width_bytes = 2  # Polly's output is a stream of 16-bits (2 bytes) samples

    def get_audio(self, text):
        try:
            session = Session()
            polly = session.client("polly")
            response = polly.synthesize_speech(Text=text,
                                               OutputFormat="pcm",
                                               VoiceId="Vitoria",
                                               LanguageCode="pt-BR",
                                               TextType="text",
                                               SampleRate="16000")
            memory_file = BytesIO()

            frames = []
            stream = response.get("AudioStream")
            frames.append(stream.read())

            wave_file = wave.open(memory_file, 'wb')
            wave_file.setnchannels(self.auido_channels)
            wave_file.setsampwidth(self.audio_sample_width_bytes)
            wave_file.setframerate(self.rate)
            wave_file.writeframes(b''.join(frames))
            wave_file.close()
            memory_file.seek(0)
            return memory_file.read()
        except (BotoCoreError, ClientError) as error:
            log.error(f"Erro ao processar audio - {error}")
