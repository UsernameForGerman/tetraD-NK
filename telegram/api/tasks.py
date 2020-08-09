from django.conf import settings

from requests import Session
import os

from core.celery import app

@app.task(queue='telegram')
def send_message(chat_id, text='') -> str:
    s = Session()
    # telegram_url = os.environ.get('TELEGRAM_URL')
    # telegram_token = os.environ.get('TELEGRAM_TOKEN')
    url = '{url}/bot{token}/sendMessage'.format(url=settings.TELEGRAM_URL, token=settings.TELEGRAM_TOKEN)
    #url = 'https://api.telegram.org/bot1154390364:AAETocdNSsgmW5RJ5pu_U45_wJr76m6r4vQ/sendMessage'
    print(url)
    print('send telegram cms {} {}'.format(chat_id, text))
    r = s.post(url, data={'chat_id': chat_id, 'text': text})

    return '{}\n{}'.format(r.status_code, r.text)

