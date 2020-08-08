from django.conf import settings

from requests import Session
import os

from core.celery import app

TELEGRAM_URL = os.environ.get('TELEGRAM_URL')
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')

@app.task(queue='telegram')
def send_message(chat_id, text='') -> None:
    s = Session()
    url = '{url}/bot{token}/sendMessage'.format(url=TELEGRAM_URL, token=TELEGRAM_TOKEN)
    print('send telegram cms {} {}'.format(chat_id, text))
    s.post(url, data={'chat_id': chat_id, 'text': text})

