from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.shortcuts import redirect, reverse
from django.contrib.auth.models import User

from .forms import CreateTaskWithDetailedAnswerForm, CreateTaskWithShortAnswerForm, AnswerTaskForm
from .models import TaskModel, Answer


def index(request):
    return HttpResponse('Main page or tasks app')


def answer_page(request, pk):
    if not request.user.is_authenticated:
        return redirect(reverse('login_page'))
    if request.method == 'POST':
        form = AnswerTaskForm(request.POST)
        if form.is_valid():
            a = Answer.objects.create(
                text=form.cleaned_data['text'],
                responding_user=request.user,
                task=TaskModel.objects.get(pk=pk)
            )
            return redirect(reverse('task', kwargs={'pk': pk}))
    else:
        form = AnswerTaskForm()
    return render(request, 'tasks/answer_task.html',
                  {'form': form, 'action_url': reverse('answer_task', kwargs={'pk': pk})})


def _create_task(request, Form, template_dir, action_url, get_reference_short_answer=False):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            task = TaskModel.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                reference_short_answer=form.cleaned_data[
                    'reference_short_answer'] if get_reference_short_answer else '',
                user=request.user
            )

            return redirect(reverse('task', kwargs={'pk': task.pk}))
    else:
        form = Form()
    return render(request, template_dir, {'form': form, 'action_url': action_url})


def create_detail_task(request):
    return _create_task(request, CreateTaskWithDetailedAnswerForm, 'tasks/create_detail_task.html',
                        reverse('create_detail_task'))


def create_short_task(request):
    return _create_task(request, CreateTaskWithShortAnswerForm, 'tasks/create_short_task.html',
                        reverse('create_short_task'), get_reference_short_answer=True)


class TasksList(ListView):
    model = TaskModel
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks_list'
    paginate_by = 5
    ordering = '-created_at'


class Task(DetailView):
    model = TaskModel
    template_name = 'tasks/task.html'
    context_object_name = 'task'
