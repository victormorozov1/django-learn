from django.contrib import admin
from django.urls import path, include
from users.views import AllUsers, OneUser, user_page, register_page, enter_page

urlpatterns = [
    path('', AllUsers.as_view(), name='users'),
    path('user/<int:pk>', OneUser.as_view(), name='user_page'),
    path('register/', register_page, name='register_page'),
    path('enter/', enter_page, name='enter_page'),
]
