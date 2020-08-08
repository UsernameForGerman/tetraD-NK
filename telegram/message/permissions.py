from rest_framework.permissions import BasePermission
from django.conf import settings

class TelegramUserPermission(BasePermission):
    """
    Global permission check for telegram token.
    """

    def has_permission(self, request, view, *args, **kwargs):
        return view.kwargs.get('token') == str(settings.TELEGRAM_TOKEN)