from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.shortcuts import redirect, reverse

from .models import Task
from .forms import CreateTaskWithDetailedAnswerForm, CreateTaskWithShortAnswerForm
from .models import Task


def index(request):
    return HttpResponse('Main page or tasks app')


def _create_task(request, Form, template_dir, get_detail_answer=False, get_reference_short_answer=False):
    if request.method == 'POST':
        form = Form(request.POST)
        task = Task.objects.create(
            title=form.clecned_data['title'],
            description=form.clecned_data['description'],
            reference_short_answer=form.cleaned_data['reference_short_answer'] if get_reference_short_answer else '',
            detail_answer=form.cleaned_data['detail_answer'] if get_detail_answer else ''
        )
        return redirect(reverse('task', task.pk))
    else:
        form = Form()
        return render(request, template_dir, {'form': form})


def create_detail_task(request):
    return _create_task(request, CreateTaskWithDetailedAnswerForm, 'tasks/create_detail_task.html',
                        get_detail_answer=True)


def create_short_task(request):
    return _create_task(request, CreateTaskWithDetailedAnswerForm, 'tasks/create_short_task.html',
                        get_reference_short_answer=True)


class TasksList(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks_list'
    paginate_by = 5


class Task(DetailView):
    model = Task
    template_name = 'tasks/task.html'
    context_object_name = 'task'
