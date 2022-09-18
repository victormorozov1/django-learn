from django.forms import ModelForm

from .models import Task


# style = forms.TextInput(attrs={'class': 'form-control'})


class CreateTaskWithShortAnswerForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'reference_short_answer']


class CreateTaskWithDetailedAnswerForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
