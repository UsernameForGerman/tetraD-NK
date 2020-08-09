from rest_framework.views import APIView
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_403_FORBIDDEN
from rest_framework.response import Response

from .models import Admin

class AdminRegisterView(APIView):

    def post(self, *args, **kwargs):
        try:
            username = self.request.data.get('username')
            password = self.request.data.get('password')
            chat_id = self.request.data.get('chat_id')
        except (AttributeError, KeyError, TypeError) as e:
            return Response(str(e), status=HTTP_400_BAD_REQUEST)

        admin = Admin.objects.filter(username=username, password=password).first()

        if admin:
            if admin.chat_id and admin.chat_id == chat_id:
                return Response('Admin {} already existed'.format(username), status=HTTP_200_OK)
            else:
                admin.chat_id = chat_id
                admin.save(update_fields=('chat_id', ))
                return Response('Admin {} registered'.format(username), status=HTTP_200_OK)
        else:
            return Response(status=HTTP_403_FORBIDDEN)

