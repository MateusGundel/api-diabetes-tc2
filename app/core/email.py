import logging
from app.core.config import settings

log = logging.getLogger(__name__)


# async def send_email_validacao_async(subject: str, email_to: str, body: str):
#     message = MessageSchema(
#         subject=subject,
#         recipients=[email_to],
#         body=body,
#         subtype='html',
#     )

#     conf = ConnectionConfig(MAIL_USERNAME=settings.MAIL_USERNAME,
#                             MAIL_PASSWORD=settings.MAIL_PASSWORD,
#                             MAIL_FROM=email_from,
#                             MAIL_PORT=settings.MAIL_PORT,
#                             MAIL_SERVER=settings.MAIL_SERVER,
#                             MAIL_TLS=True,
#                             MAIL_SSL=False,
#                             USE_CREDENTIALS=True,
#                             TEMPLATE_FOLDER='app/templates/email')
#     fm = FastMail(conf)
#     await fm.send_message(message, template_name='email.html')


# async def send_email_validacao_async(subject: str, email_to: str, body: dict):
#     message = MessageSchema(
#         subject=subject,
#         recipients=[email_to],
#         template_body=body
#     )
#     conf = ConnectionConfig(MAIL_USERNAME=settings.MAIL_USERNAME,
#                             MAIL_PASSWORD=settings.MAIL_PASSWORD,
#                             MAIL_FROM=settings.MAIL_USERNAME,
#                             MAIL_PORT=settings.MAIL_PORT,
#                             MAIL_SERVER=settings.MAIL_SERVER,
#                             MAIL_TLS=True,
#                             MAIL_SSL=False,
#                             USE_CREDENTIALS=True,
#                             TEMPLATE_FOLDER='app/templates/email')
#     fm = FastMail(conf)
#     await fm.send_message(message, template_name='validacao.html')
