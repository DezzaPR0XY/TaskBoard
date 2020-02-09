from django.db import models
from login_reg.models import User

# Create your models here.
class Task(models.Model):
  title = models.CharField(max_length=255)
  details = models.TextField()
  created_date = models.DateTimeField(auto_now=True)
  updated_date = models.DateTimeField()
  due_date = models.DateTimeField()
  status = [
    (complete, "Complete"),
    (hold, "Hold"),
    (to_do, "To Do"),
    (in_prog, "In Progress")
  ]
  tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

class Taskboard(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField()
  creator = models.OneToOneField(User, on_delete=models.CASCADE)
  created_date = models.DateTimeField(auto_now=True)
  task = models.ForeignKey(Task, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

class Tag(models.Model):
  name = models.CharField(max_length=255)
