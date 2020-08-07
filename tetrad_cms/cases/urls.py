from django.urls.conf import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

# local
from .viewsets import CaseViewSet, ContactViewSet

router = DefaultRouter()
router.register('cases', CaseViewSet)
router.register('contact', ContactViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]