from django.db import models


class User(models.Model):
    max_password_len = 123

    name = models.CharField(max_length=17)
    password = models.CharField(max_length=max_password_len, blank=True)
    hashed_password = models.CharField(max_length=max_password_len)

    def __str__(self):
        return f'User {self.name}'
