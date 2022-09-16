from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.forms.utils import ErrorList
from django import forms
from django.core.exceptions import ValidationError
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth import login
import django.contrib.auth.hashers

from .models import Profile
from .forms import RegisterForm, LoginForm, EnterForm
from .hash import hash


HASH_FUNC = hash


class AllUsers(ListView):
    model = User
    template_name = 'users/main_page.html'
    context_object_name = 'users'
    paginate_by = 5


class OneUser(DetailView):
    model = User
    template_name = 'users/user_page.html'
    context_object_name = 'user'


def register_page(request):
    if request.method == 'GET':
        register_form = RegisterForm()
    else:
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            pass1_hash, pass2_hash = HASH_FUNC(register_form.cleaned_data['password']), HASH_FUNC(
                register_form.cleaned_data['repeat_password'])  # make_password каждый раз делает разные пароли

            user = User.objects.create(username=register_form.cleaned_data['name'], password=pass1_hash)
            Profile.objects.create(about='-', hobby='-', user=user)
            return render(request, 'users/success_registration.html')

    return render(request, 'users/register.html', {'form': register_form})


# def login_page(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('users')
#         else:
#             print('wrong')
#
#     else:
#         form = LoginForm()
#     return render(request, 'users/enter.html', {'form': form})

def login_page(request):
    if request.method == 'GET':
        enter_form = EnterForm()
    else:
        enter_form = EnterForm(request.POST)
        # print(enter_form.cleaned_data['password'])

        # print(hash(enter_form.cleaned_data['password']))
        # print(user.hashed_password)
        if enter_form.is_valid():
            user = User.objects.get(username=enter_form.cleaned_data['name'])
            print('SUCCESS ENTER')
            login(request, user)

    return render(request, 'users/enter.html', {'form': enter_form})
