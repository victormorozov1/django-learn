from django import forms

from .models import Task


style = forms.TextInput(attrs={'class': 'form-control'})


class CreateTaskWithShortAnswerForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'reference_short_answer']
        widgets = {
            'title': style,
            'description': style,
            'reference_short_answer': style,
        }


class CreateTaskWithDetailedAnswerForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        widgets = {
            'title': style,
            'description': style,
        }
