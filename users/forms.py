from django import forms
from .models import User


class RegisterForm(forms.Form):
    style = forms.TextInput(attrs={'class': 'form-control'})

    name = forms.CharField(max_length=User.max_name_len, widget=style)
    password = forms.CharField(max_length=User.max_password_len, widget=style)
    repeat_password = forms.CharField(max_length=User.max_password_len, widget=style)
