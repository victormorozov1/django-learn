from django.contrib import admin
from django.urls import path, include
from users.views import main_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
]
