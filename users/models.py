from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # change on_delete
    about = models.TextField()
    hobby = models.CharField(max_length=120)

# class User(models.Model):
#     max_password_len = 123
#     max_name_len = 20
#
#     name = models.CharField(max_length=max_name_len)
#     password = models.CharField(max_length=max_password_len, blank=True)
#     hashed_password = models.IntegerField()
#
#     def get_absolute_url(self):
#         return reverse('user_page', kwargs={'pk': self.pk})
#
#     def __str__(self):
#         return f'User {self.name}'


