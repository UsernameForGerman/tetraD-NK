from django.urls import path
from django.conf import settings

import os

from .views import SendContactsView

urlpatterns = [
    path('send/contact', SendContactsView.as_view(), name='webhook-view'),
]
