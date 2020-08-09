from django.conf import settings

from requests import Session
import os

from core.celery import app

@app.task(queue='telegram')
def send_message(chat_id, text='') -> str:
    s = Session()
    url = '{url}bot{token}/sendMessage'.format(url=settings.TELEGRAM_URL, token=settings.TELEGRAM_TOKEN)
    r = s.post(url, data={'chat_id': chat_id, 'text': text})

    return '{}\n{}'.format(r.status_code, r.text)

