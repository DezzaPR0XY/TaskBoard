from django.db import models
from process.models import Taskboard, Task

# Create your models here.
class User(models.Model):
  name_first = models.CharField(max_length=255)
  name_last = models.CharField(max_length=255)
  email = models.EmailField()
  date_created = models.DateTimeField()
  password = models.CharField(max_length=255)