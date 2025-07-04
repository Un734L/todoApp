from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required

# Create your views here.
#CRUD
@login_required
def taskCreateView(request):
    if request.method=="POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form=TaskForm()
    return render(request,'todoApp/task_create.html',{'form':form})

@login_required
def taskListView(request):
    tasks=Task.objects.filter(user=request.user.username).order_by('date_recorded')
    return render(request,'todoApp/task_list.html',{'tasks':tasks})

@login_required
def taskUpdateView(request,task_id):
    pass

@login_required
def taskDeleteView(request,task_id):
    pass

@login_required
def taskDetailsView(request,task_id):
    pass

@login_required
def taskCompleteView(request,task_id):
    pass