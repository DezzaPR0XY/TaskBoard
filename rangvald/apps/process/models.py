from django.db import models
from login_reg.models import User

# Create your models here.
# For a FKey does "this" need another relationship on create
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
  tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="tasks_w_tag")
  poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserTasks")

  def __str__(self):
    return self.title

class Taskboard(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField()
  created_date = models.DateTimeField(auto_now=True)
  task = models.ForeignKey(Task, on_delete=models.CASCADE)
  creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserTaskLists")
  other_users = models.ManyToManyField(User, related_name="Taskboards")

class Tag(models.Model):
  name = models.CharField(max_length=255)

class Perms(models.Model):
  taskboard = models.ForeignKey(Taskboard, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  level = models.IntegerField()
  description = models.TextField(max_length=255)