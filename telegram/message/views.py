from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from django.conf import settings

from requests import Session

from .permissions import TelegramUserPermission
from api.tasks import send_message, register_new_admin_chat_id

class WebhookView(APIView):
    permission_classes = (TelegramUserPermission, )

    def post(self, *args, **kwargs):
        try:
            chat_id = self.request.data.get('message').get('chat').get('id')
            text = self.request.data.get('message').get('text')
        except (TypeError, KeyError, AttributeError) as e:
            return Response(str(e), status=HTTP_400_BAD_REQUEST)

        if text == '/admin':
            text = 'Write your password in this template:\nPassword : my_password'
            send_message.apply_async(kwargs={'chat_id': chat_id, 'text': text})
        elif 'Password : ' in text:
            try:
                username = self.request.data.get('message').get('chat').get('username')
            except (TypeError, KeyError, AttributeError) as e:
                return Response(str(e), status=HTTP_400_BAD_REQUEST)
            register_new_admin_chat_id.apply_async(kwargs={
                'chat_id': chat_id,
                'username': username,
                'password': text.split(' : ')[1]
            })
        else:
            send_message.apply_async(kwargs={'chat_id': chat_id, 'text': text})

        return Response(status=HTTP_200_OK)

