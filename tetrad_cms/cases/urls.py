from django.urls.conf import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

# local
from .viewsets import CaseViewSet, ContactViewSet
from .views import AdminRegisterView

router = DefaultRouter()
router.register('cases', CaseViewSet)
router.register('contact', ContactViewSet)

urlpatterns = [
    path('register/admin', AdminRegisterView.as_view(), name='register-admin'),
    url(r'^', include(router.urls))
]