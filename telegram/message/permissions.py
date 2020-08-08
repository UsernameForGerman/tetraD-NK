from rest_framework import permissions
from django.conf import settings

class TelegramUserPermission(permissions.BasePermission):
    """
    Global permission check for telegram token.
    """

    def has_permission(self, request, view, *args, **kwargs):
        return view.kwargs.get('token') == str(settings.TELEGRAM_TOKEN)