from django.contrib import admin
from django.urls import path, include
from users.views import main_page, user_page, register_page

urlpatterns = [
    path('', main_page, name='users'),
    path('user/<int:user_id>', user_page, name='user_page'),
    path('register/', register_page, name='register_page')
]
