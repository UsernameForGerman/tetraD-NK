from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from django.conf import settings

from requests import Session

from .tasks import send_message

class SendContactsView(APIView):
    template = "New contact info send to you from {host}!\nContact info: {contact}"

    def post(self, *args, **kwargs):
        try:
            contact = self.request.data.get('contact').get('contact')
            admins = [admin.get('chat_id', '') for admin in self.request.data.get('admins')]
        except (KeyError, AttributeError) as e:
            return Response(e, status=HTTP_400_BAD_REQUEST)

        data_to_send = self.template.format(
            host=self.request.META.get('HTTP_HOST', 'Unknown'),
            contact=contact
        )

        for admin in admins:
            send_message.delay(admin, data_to_send)

        return Response(status=HTTP_200_OK)

