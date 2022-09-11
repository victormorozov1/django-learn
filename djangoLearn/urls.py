from django.contrib import admin
from django.urls import path, include
from users.views import main_page
from .views import home_page
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('users/', include('users.urls')),
]
