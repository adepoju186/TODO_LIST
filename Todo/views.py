from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
import logging
logger = logging.getLogger(__name__)


# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    return render(request,'task_list.html', {'tasks':tasks})

def task_detail(request,pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task':task})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list' )
        
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(instance=task)
    if request.method =='POST':
        form =TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
            return redirect(reverse('task_detail', kwargs={'pk': task.pk}))
        
        else:
             form = TaskForm(instance=task)
             
    return render(request, 'task_form.html',{'form':form})
    
def task_delete(request, pk):
        task = get_object_or_404(Task, pk =pk)
        if request.method =='POST':
            task.delete()
            return redirect('task_list')
        return render(request, 'task_confirm_delete.html', {'task':task})   