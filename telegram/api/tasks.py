from django.conf import settings

from requests import Session
from json import dumps

from core.celery import app

@app.task(queue='telegram')
def send_message(chat_id, text='') -> None:
    s = Session()
    url = '{url}bot{token}/sendMessage'.format(url=settings.TELEGRAM_URL, token=settings.TELEGRAM_TOKEN)
    s.post(url, data={'chat_id': chat_id, 'text': text})

@app.task(queue='cms_api')
def register_new_admin_chat_id(chat_id, username='', password='') -> None:
    s = Session()
    url = '{url}auth'.format(url=settings.CMS_URL)
    data = {'chat_id': chat_id, 'username': username, 'password': password}
    try:
        response = s.post(url, data=dumps(data), headers={'Content-Type': 'application/json'})
    except BaseException as e:
        send_message.delay(kwargs={'chat_id': chat_id, 'text': 'We are sorry, tetradnk.ru unavailable :('})
        return

    if response.status_code == 403:
        send_message.delay(kwargs={'chat_id': chat_id, 'text': 'You are not registered as admin'})
    elif response.status_code == 200:
        send_message.delay(kwargs={'chat_id': chat_id, 'text': response.text})
    else:
        send_message.delay(kwargs={'chat_id': chat_id, 'text': 'Some server errors occured. Sorry :('})
