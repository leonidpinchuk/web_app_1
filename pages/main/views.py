from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html') #, {'title': 'Main list', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def dashboard(request):
    tasks = Task.objects.order_by('-id')

    form = TaskForm()
    context = {
        'form': form,
        'title': 'Comment',
        'tasks': tasks
    }
    return render(request, 'main/dashboard.html', context)


