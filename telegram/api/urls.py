from django.urls import path
from django.conf import settings

import os

from .views import WebhookView

urlpatterns = [
    path('<str:token>', WebhookView.as_view(), name='webhook-view'),
]
