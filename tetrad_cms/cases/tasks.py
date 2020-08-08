from django.conf import settings

from requests import Session

from core.celery import app

TELEGRAM_BOT_API_URL = 'http://telegram:5000/'

if settings.TELEGRAM_BOT_API_URL:
    print('Env telegram bot api url')
    tg_bot_api_url = settings.TELEGRAM_BOT_API_URL
else:
    print('Ooops!')
    tg_bot_api_url = TELEGRAM_BOT_API_URL



@app.task(queue='cms')
def send_new_contact_to_admins(contact: dict, admins: list) -> None:
    s = Session()
    print('sending from cms {} {}'.format(admins, contact))
    s.post(tg_bot_api_url + 'send/contact', data={'admins': admins, 'contact': contact})

