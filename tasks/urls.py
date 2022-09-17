from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('/task_list', TasksList.as_view(), name='tasks_list')
]
