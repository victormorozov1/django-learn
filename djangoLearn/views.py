from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


def home_page(request):
    return render(request, 'home_page.html')


