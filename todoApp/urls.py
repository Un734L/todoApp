from django.urls import path
from . import views 

app_name="todoApp"

urlpatterns=[
    path('create/',views.taskCreateView,name='task_create'),
    path('tasks/',views.taskListView,name='task_list'),
    path('complete/<int:task_id>/',views.taskListView,name='task_complete'),
    path('update/<int:task_id>/',views.taskUpdateView,name='task_update'),
    path('delete/<int:task_id>/',views.taskDeleteView,name='task_delete'),
]