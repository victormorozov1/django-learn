from django.db import models
from django.urls import reverse


class User(models.Model):
    max_password_len = 123
    max_name_len = 20

    name = models.CharField(max_length=max_name_len)
    password = models.CharField(max_length=max_password_len, blank=True)
    hashed_password = models.IntegerField()

    def get_absolute_url(self):
        return reverse('user_page', kwargs={'user_id': self.pk})

    def __str__(self):
        return f'User {self.name}'


