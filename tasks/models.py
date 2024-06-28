from django.db import models

# Create your models here.
class Tasks(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(null=True, blank=True)
  completed = models.BooleanField(default=False)
  due_date = models.DateField(null=True, blank=True)