from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from django.conf import settings

from json import loads
from requests import Session

from .permissions import TelegramUserPermission

class WebhookView(APIView):
    permission_classes = (TelegramUserPermission, )

    def post(self, *args, **kwargs):
        print(self.request.data)
        try:
            chat_id = self.request.data.get('message').get('chat').get('id')
            text = self.request.data.get('message').get('text')
        except (TypeError, KeyError, AttributeError) as e:
            print(e)
            return Response(e, status=HTTP_400_BAD_REQUEST)

        s = Session()
        url = "{}bot{}/sendMessage".format(settings.TELEGRAM_URL, settings.TELEGRAM_TOKEN)
        print(url)
        data = {
            'chat_id': chat_id,
            'text': text,
        }
        print(data)
        response = s.post(url, data=data)

        print(response.status_code)
        print(response.text)

        return Response(status=HTTP_200_OK)

