from django.shortcuts import render
from django.http import HttpResponse


def main_page(request):
    return HttpResponse("Main page og users App.")
