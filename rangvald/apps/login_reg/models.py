from django.db import models
from process.models import Taskboard, Task

# Create your models here.
class User(models.Model):
  name_first = models.CharField(max_length=255)
  name_last = models.CharField(max_length=255)
  email = models.EmailField()
  date_created = models.DateTimeField()
  password = models.CharField(max_length=255)
  task = models.ForeignKey(Task, on_delete=models.CASCADE)
  taskboard = models.ForeignKey(Taskboard, on_delete=models.CASCADE)

class Perms(models.Model):
  taskboard = models.ForeignKey(Taskboard, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  level = models.IntegerField()
  description = models.TextField(max_length=255)