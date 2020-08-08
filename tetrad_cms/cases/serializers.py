from rest_framework.serializers import ModelSerializer, SerializerMethodField

# local
from .models import Case, Task, Contact, Admin

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('task', )

class CaseSerializer(ModelSerializer):
    tasks = SerializerMethodField()

    class Meta:
        model = Case
        exclude = ('modified', )

    def get_tasks(self, case):
        return TaskSerializer(Task.objects.filter(case=case), many=True).data

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ('contact', )

class AdminSerializer(ModelSerializer):
    chat_id = SerializerMethodField()

    class Meta:
        model = Admin
        fields = ('chat_id', )

    def get_chat_id(self, admin):
        chat_id = admin.chat_id
        try:
            return int(chat_id)
        except ValueError:
            pass

        return chat_id
