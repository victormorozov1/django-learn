from django.forms import ModelForm

from .models import Task


class CreateTaskWithShortAnswerForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'reference_short_answer']


class CreateTaskWithDetailedAnswerForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
