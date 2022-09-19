from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.forms.utils import ErrorList
from django import forms
from django.core.exceptions import ValidationError
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
import django.contrib.auth.hashers
from django.urls import reverse

from .models import Profile
from .forms import RegisterForm, EnterForm
from .hash import hash


class AllUsers(ListView):
    model = User
    template_name = 'users/main_page.html'
    context_object_name = 'users'
    paginate_by = 5


class OneUser(DetailView):
    model = User
    template_name = 'users/user_page.html'
    context_object_name = 'user'


# action_url в register_page и login_page передается потому,
# что невозможно использовать функцию url в шаблоне в нужном месте
def register_page(request):
    if request.method == 'GET':
        register_form = RegisterForm()
    else:
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            pass1_hash, pass2_hash = hash(register_form.cleaned_data['password']), hash(
                register_form.cleaned_data['repeat_password'])  # make_password каждый раз делает разные пароли

            user = User.objects.create(username=register_form.cleaned_data['name'], password=pass1_hash)
            Profile.objects.create(about='-', hobby='-', user=user)
            return render(request, 'users/success_registration.html')

    return render(request, 'users/register.html', {'form': register_form, 'action_url': reverse('register_page')})


def login_page(request):
    if request.method == 'GET':
        enter_form = EnterForm()
    else:
        enter_form = EnterForm(request.POST)
        if enter_form.is_valid():
            for i in range(100):
                print('is valid')
            user = User.objects.get(username=enter_form.cleaned_data['name'])
            print('SUCCESS ENTER')
            login(request, user)
            # print(reverse('users', kwargs={'pk': 1}))
            return redirect(reverse('user_page', kwargs={'pk': user.pk}))

    return render(request, 'users/enter.html', {'form': enter_form, 'action_url': reverse('login_page')})


def logout_page(request):
    logout(request)
    return redirect('home')
