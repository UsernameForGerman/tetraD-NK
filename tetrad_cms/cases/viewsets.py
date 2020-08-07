from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

# local
from .serializers import CaseSerializer, ContactSerializer
from .models import Case, Contact

class CaseViewSet(ReadOnlyModelViewSet):
    serializer_class = CaseSerializer
    queryset = Case.objects.all()
    lookup_field = 'case'

class ContactViewSet(ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    lookup_field = 'contact'

