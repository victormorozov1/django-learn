from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from users.models import User


def main_page(request):
    return render(request, 'users/main_page.html')


def user_page(request, user_id):
    print('USER OAGE GETTED')
    return render(request, 'users/user_page.html', {'user': get_object_or_404(User, pk=user_id)})
