from django.contrib import admin
from django.urls import path, include
from users.views import AllUsers, OneUser, register_page, login_page, logout_page

urlpatterns = [
    path('', AllUsers.as_view(), name='users'),
    path('user/<int:pk>', OneUser.as_view(), name='user_page'),
    path('register/', register_page, name='register_page'),
    path('enter/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page')
]
