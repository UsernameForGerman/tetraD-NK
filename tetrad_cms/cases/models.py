from django.db import models
from cms.models import CMSPlugin
from django.utils import timezone

class Case(models.Model):
    title = models.CharField(unique=True, max_length=64, db_index=True)
    image = models.ImageField(upload_to='cases/', editable=True)
    description = models.TextField(max_length=128, null=True, blank=True)
    goal = models.CharField(max_length=64)
    solution = models.CharField(max_length=128)
    duration = models.CharField(max_length=32, blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    link = models.URLField(null=True, blank=True)
    presentation = models.FileField('Presentation file', upload_to='presentations/', blank=True, null=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        # if not self.id:
        #     self.created = timezone.now()
        self.modified = timezone.now()
        return super(Case, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Task(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    task = models.CharField(max_length=64)

    def __str__(self):
        return "{} <- {}".format(self.case.title, self.task)

class Contact(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    contact = models.TextField(max_length=512)

    def __str__(self):
        return self.contact

class CasePluginModel(CMSPlugin):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)

    def __str__(self):
        return self.case.title

class Admin(models.Model):
    chat_id = models.CharField(max_length=256, unique=True, db_index=True)

    def __str__(self):
        return self.chat_id



