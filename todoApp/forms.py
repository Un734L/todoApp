from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = [
            'task_title',
            'task_description',
            'isCompleted'
        ]

        labels={
            'task_title':'Title',
            'task_description':'Description',
            'isCompleted':'Check If Task Is Completed:',
        }