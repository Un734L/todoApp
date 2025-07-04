from django.urls import path
from . import views 

urlpatterns=[
    path('create/',views.taskCreateView,name='task_create'),
    path('tasks/',views.taskListView,name='task-list'),
    """path(),
    path(),
    path(),"""
]