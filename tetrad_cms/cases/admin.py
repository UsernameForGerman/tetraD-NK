from django.contrib import admin
from .models import CasePluginModel, Case, Contact, Task
# Register your models here.

admin.site.register(CasePluginModel)
admin.site.register(Case)
admin.site.register(Contact)
admin.site.register(Task)
