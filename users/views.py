from django.shortcuts import render
from django.http import HttpResponse
from users.models import User


def main_page(request):
    return render(request, 'users/main_page.html')


def user_page(request, user_id):
    print('USER OAGE GETTED')
    return render(request, 'users/user_page.html', {'user': User.objects.get(id=user_id)})
