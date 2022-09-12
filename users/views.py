from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import User
from .forms import RegisterForm, EnterForm
from .hash import hash
from django.forms.utils import ErrorList
from django import forms
from django.core.exceptions import ValidationError


def main_page(request):
    return render(request, 'users/main_page.html')


def user_page(request, user_id):
    print('USER OAGE GETTED')
    return render(request, 'users/user_page.html', {'user': get_object_or_404(User, pk=user_id)})


def register_page(request):
    if request.method == 'GET':
        register_form = RegisterForm()
    else:
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            pass1_hash, pass2_hash = hash(register_form.cleaned_data['password']), hash(
                register_form.cleaned_data['repeat_password'])

            User.objects.create(name=register_form.cleaned_data['name'], hashed_password=pass1_hash)
            return render(request, 'users/success_registration.html')

    return render(request, 'users/register.html', {'form': register_form})


def enter_page(request):
    if request.method == 'GET':
        enter_form = EnterForm()
    else:
        enter_form = EnterForm(request.POST)
        if enter_form.is_valid():
            print(enter_form.cleaned_data['password'])
            print(hash(enter_form.cleaned_data['password']))
            print(User.objects.get(
                    name=enter_form.cleaned_data['name']).hashed_password)
            if hash(enter_form.cleaned_data['password']) == User.objects.get(
                    name=enter_form.cleaned_data['name']).hashed_password:
                print('SUCCESS ENTER')
    return render(request, 'users/enter.html', {'form': enter_form})
