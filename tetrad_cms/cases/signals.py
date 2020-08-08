from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Contact, Admin
from django.conf import settings

from .tasks import send_new_contact_to_admins as send_contact
from .serializers import AdminSerializer, ContactSerializer

@receiver(post_save, sender=Contact)
def send_new_contact_to_admins(sender, instance, **kwargs):
    admins = Admin.objects.all()
    admins_chat_id = AdminSerializer(admins, many=True).data
    contact = ContactSerializer(instance, many=False).data

    print('sending from cms {} {}'.format(admins_chat_id, contact))
    send_contact.delay(contact, admins_chat_id)
