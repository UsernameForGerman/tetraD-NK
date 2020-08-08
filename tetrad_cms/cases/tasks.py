from django.conf import settings

from requests import Session
import os
from json import dumps

from core.celery import app

TELEGRAM_BOT_API_URL = os.environ.get('TELEGRAM_BOT_API_URL')

@app.task(queue='cms')
def send_new_contact_to_admins(contact: dict, admins: list) -> None:
    s = Session()
    print('sending from cms {} {}'.format(admins, contact))
    data = {'admins': admins, 'contact': contact}
    url = TELEGRAM_BOT_API_URL + 'send/contact'
    s.post(url, data=dumps(data), headers={'Content-Type': 'application/json'})

