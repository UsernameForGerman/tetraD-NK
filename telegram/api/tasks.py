from django.conf import settings

from requests import Session
import os

from core.celery import app

@app.task(queue='telegram')
def send_message(chat_id, text='') -> None:
    s = Session()
    telegram_url = os.environ.get('TELEGRAM_URL')
    telegram_token = os.environ.get('TELEGRAM_TOKEN')
    url = '{url}/bot{token}/sendMessage'.format(url=telegram_url, token=telegram_token)
    print('send telegram cms {} {}'.format(chat_id, text))
    s.post(url, data={'chat_id': chat_id, 'text': text})

