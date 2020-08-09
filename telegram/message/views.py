from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from django.conf import settings

from requests import Session

from .permissions import TelegramUserPermission
from api.tasks import send_message

class WebhookView(APIView):
    permission_classes = (TelegramUserPermission, )

    def post(self, *args, **kwargs):
        try:
            chat_id = self.request.data.get('message').get('chat').get('id')
            text = self.request.data.get('message').get('text')
        except (TypeError, KeyError, AttributeError) as e:
            return Response(str(e), status=HTTP_400_BAD_REQUEST)

        print(chat_id)

        send_message.delay(chat_id, text)

        return Response(status=HTTP_200_OK)

