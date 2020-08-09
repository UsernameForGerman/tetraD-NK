from django.conf import settings

from requests import Session
import os
from json import dumps

from core.celery import app

@app.task(queue='cms')
def send_new_contact_to_admins(contact: dict, admins: list) -> None:
    if settings.TELEGRAM_BOT_API_URL:
        print('bot api url')
    else:
        print('bot api not found')
    s = Session()
    data = {'admins': admins, 'contact': contact}
    url = 'http://telegram:5000/send/contact'
    s.post(url, data=dumps(data), headers={'Content-Type': 'application/json'})

