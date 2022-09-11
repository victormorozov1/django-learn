from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import User
from .forms import RegisterForm


def main_page(request):
    return render(request, 'users/main_page.html')


def user_page(request, user_id):
    print('USER OAGE GETTED')
    return render(request, 'users/user_page.html', {'user': get_object_or_404(User, pk=user_id)})


def register_page(request):
    if request.method == 'GET':
        register_form = RegisterForm()
        return render(request, 'users/register.html', {'form': register_form})
    else:
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
        return render(request, 'users/success_registration.html')

