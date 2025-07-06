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
            task_title=form.cleaned_data.get('task_title')
            task_description=form.cleaned_data.get('task_description')
            isCompleted=form.cleaned_data.get('isCompleted')
            task=Task.objects.create(task_title=task_title,task_description=task_description,isCompleted=isCompleted,user=request.user)
            task.save()
            return redirect('todoApp:task_list')
    else:
        form=TaskForm()
    return render(request,'todoApp/task_create.html',{'form':form})

@login_required
def taskListView(request):
    tasks=Task.objects.filter(user=request.user).order_by('date_recorded')
    completedTasks=list()
    uncompletedTasks=list()
    for task in tasks:
        if task.isCompleted==True:
            completedTasks.append(task)
        else:
            uncompletedTasks.append(task)
    return render(request,'todoApp/task_list.html',{'completedTasks':completedTasks,'uncompletedTasks':uncompletedTasks})

@login_required
def taskUpdateView(request,task_id):
    task=Task.objects.get(user=request.user,id=task_id)
    if request.method=="POST":
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            task_title=form.cleaned_data.get('task_title')
            task_description=form.cleaned_data.get('task_description')
            isCompleted=form.cleaned_data.get('isCompleted')
            task=Task.objects.create(task_title=task_title,task_description=task_description,isCompleted=isCompleted,user=request.user)
            task.save()
            return redirect('todoApp:task_list')
    else:
        form=TaskForm()
    return render(request,'todoApp/task_update.html',{'form':form})

@login_required
def taskDeleteView(request,task_id):
    task=Task.objects.get(user=request.user,id=task_id)
    if request.method=="POST":
        task.delete()
        return redirect('todoApp:task_list')
    return render(request,'todoApp/delete.html',{'task':task})

@login_required
def taskDetailsView(request,task_id):
    pass

@login_required
def taskCompleteView(request,task_id):
    task=Task.objects.filter(user=request.user,id=task_id)
    task.isCompleted = not task.isCompleted
    return redirect('todoApp:task_list')