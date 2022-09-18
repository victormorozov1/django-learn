from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm

from .models import User
from .hash import hash


style = forms.TextInput(attrs={'class': 'form-control'})  # Эта штука дублируется в разных приложениях


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=120, widget=style)
    password = forms.CharField(max_length=120, widget=style)
    repeat_password = forms.CharField(max_length=120, widget=style)

    def clean(self):
        form_data = self.cleaned_data
        if form_data['password'] != form_data['repeat_password']:
            self._errors["repeat_password"] = ["Password do not match"]
            form_data['repeat_password'] = ''  # Не работает почему-то !!!
        return form_data

    def clean_name(self):
        if len(User.objects.filter(username=self.cleaned_data['name'])) >= 1:
            self._errors["name"] = ["This name is already occupied"]
        return self.cleaned_data['name']


class EnterForm(forms.Form):
    name = forms.CharField(max_length=120, widget=style)
    password = forms.CharField(max_length=120, widget=style)

    def clean(self):
        form_data = self.cleaned_data
        users = User.objects.filter(username=form_data['name'])
        if len(users) > 1:
            print(f'ERROR: found {len(users)} users with name {form_data["name"]}')
        if len(users) == 0 or str(hash(form_data['password'])) != users[0].password:
            self._errors["password"] = ["Wrong username or password"]
            print(f'len(users) = {len(users)}')
            print(f'password from form: {form_data["password"]}')
            print(f'hashed password from form: {hash(form_data["password"])}')
            print(f'gash from db: {users[0].password}')
