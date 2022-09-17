from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView

from .models import Task


def index(request):
    return HttpResponse('Main page or tasks app')


class TasksList(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks_list'
    paginate_by = 5
