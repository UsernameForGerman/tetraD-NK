from django.conf import settings

from requests import Session

from core.celery import app

@app.task
def send_new_contact_to_admins(contact: dict, admins: list) -> None:
    s = Session()
    s.post(settings.TELEGRAM_BOT_API_URL + 'send/contact', data={'admins': admins, 'contact': contact})

