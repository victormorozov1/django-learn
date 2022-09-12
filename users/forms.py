from django import forms
from .models import User
from .hash import hash
from django.core.exceptions import ValidationError

style = forms.TextInput(attrs={'class': 'form-control'})


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=User.max_name_len, widget=style)
    password = forms.CharField(max_length=User.max_password_len, widget=style)
    repeat_password = forms.CharField(max_length=User.max_password_len, widget=style)

    def clean(self):
        form_data = self.cleaned_data
        if form_data['password'] != form_data['repeat_password']:
            self._errors["repeat_password"] = ["Password do not match"]
            form_data['repeat_password'] = ''  # Не работает почему-то !!!
        return form_data

    def clean_name(self):
        if len(User.objects.filter(name=self.cleaned_data['name'])) >= 1:
            self._errors["name"] = ["This name is already occupied"]
        return self.cleaned_data['name']


class EnterForm(forms.Form):
    name = forms.CharField(max_length=User.max_name_len, widget=style)
    password = forms.CharField(max_length=User.max_password_len, widget=style)

    def clean(self):
        form_data = self.cleaned_data
        user = User.objects.get(name=form_data['name'])
        if hash(form_data['password']) != user.hashed_password:
            print(
                f'pass {form_data["password"]}, hash_pass {hash(form_data["password"])}, us_h_p {user.hashed_password}')
            self._errors["password"] = ["Wrong password"]
