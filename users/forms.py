from django import forms
from .models import User


class RegisterForm(forms.Form):
    style = forms.TextInput(attrs={'class': 'form-control'})

    name = forms.CharField(max_length=User.max_name_len, widget=style)
    password = forms.CharField(max_length=User.max_password_len, widget=style)
    repeat_password = forms.CharField(max_length=User.max_password_len, widget=style)

    def clean(self):  # Function for custom validators
        form_data = self.cleaned_data
        if form_data['password'] != form_data['repeat_password']:
            self._errors["repeat_password"] = ["Password do not match"]
            form_data['repeat_password'] = ''
        return form_data
