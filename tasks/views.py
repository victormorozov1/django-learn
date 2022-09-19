from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.shortcuts import redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Q

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
            task = TaskModel.objects.get(pk=pk)
            answer = Answer(
                text=form.cleaned_data['text'],
                responding_user=request.user,
                task=task
            )
            if not task.detail_answer:
                answer.status = 'Approved' if answer.text == task.reference_short_answer else 'Rejected'
            answer.save()
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
                detail_answer=not get_reference_short_answer,
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


def change_visibility(request, answer_pk, user_pk, visibility):
    answer = get_object_or_404(Answer, pk=answer_pk)
    user = get_object_or_404(User, pk=user_pk)

    if user.pk == answer.task.user.pk:
        answer.make_public_task_admin = bool(visibility)
    if user.pk == answer.responding_user.pk:
        answer.make_public_responding_user = bool(visibility)
    answer.save()

    return redirect(reverse('task', kwargs={'pk': answer.task.pk}))


def change_answer_status(request, pk, status):
    if not request.user.is_authenticated:
        return redirect(reverse('login_page'))

    answer = Answer.objects.get(pk=pk)
    if request.user == answer.task.user:
        answer.status = status
        answer.save()
    else:
        print('Недостаточно прав')  # по хорошему нужно вывести это сообщение в html, но мне лень

    return redirect(reverse('task', kwargs={'pk': answer.task.pk}))


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        task = TaskModel.objects.get(pk=self.kwargs['pk'])
        if self.request.user.is_authenticated:
            if task.user.pk == self.request.user.pk:
                context['answers'] = Answer.objects.filter(task=task)
            else:
                context['answers'] = Answer.objects.filter(
                    Q(task=task) & Q(responding_user=self.request.user) | Q(make_public_responding_user=True) & Q(
                        make_public_task_admin=True))
        else:
            context['answers'] = Answer.objects.filter(make_public_task_admin=True, make_public_responding_user=True)

        return context
