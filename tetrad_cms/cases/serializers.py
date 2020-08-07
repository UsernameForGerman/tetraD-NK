from rest_framework.serializers import ModelSerializer, SerializerMethodField

# local
from .models import Case, Task, Contact

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
        exclude = ('created', )
