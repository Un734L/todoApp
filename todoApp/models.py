from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    
    task_title=models.CharField(max_length=100)
    task_description=models.TextField()
    isCompleted=models.BooleanField()
    date_recorded=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.task_title