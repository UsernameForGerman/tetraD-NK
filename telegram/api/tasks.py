from django.conf import settings

from requests import Session

from core.celery import app

@app.task
def send_message(chat_id, text='') -> None:
    s = Session()
    url = '{url}/bot{token}/sendMessage'.format(url=settings.TELEGRAM_URL, token=settings.TELEGRAM_TOKEN)
    s.post(url, data={'chat_id': chat_id, 'text': text})
