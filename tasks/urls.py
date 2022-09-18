from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('task_list/', TasksList.as_view(), name='tasks_list'),
    path('task<int:pk>/', Task.as_view(), name='task'),
    path('create-detail-task/', create_detail_task, name='create_detail_task'),
    path('create-short-task/', create_short_task, name='create_short_task'),
    path('answer-task<int:pk>/', answer_page, name='answer_task'),
]
