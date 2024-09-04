from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()

    # Filtering by status
    status = request.GET.get('status')
    if status:
        tasks = tasks.filter(status=status)

    # Sorting by priority or due_date
    sort_by = request.GET.get('sort_by')
    if sort_by:
        tasks = tasks.order_by(sort_by)
    
    context = {'tasks': tasks}
    return render(request, 'tasks/task_list.html', context)


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redirect to task list after creating the task
    else:
        form = TaskForm()
    
    context = {'form': form}
    return render(request, 'tasks/task_create.html', context)
