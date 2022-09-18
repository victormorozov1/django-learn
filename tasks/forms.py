from django import forms

from .models import Task


input = forms.TextInput(attrs={'class': 'form-control'})


# class CreateTaskWithShortAnswerForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['title', 'description', 'reference_short_answer']
#         widgets = {
#             'title': input,
#             'description': input,
#             'reference_short_answer': input,
#         }
#
#
# class CreateTaskWithDetailedAnswerForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['title', 'description']
#         widgets = {
#             'title': input,
#             'description': input,
#         }


class CreateTaskWithShortAnswerForm(forms.Form):
    title = forms.CharField(max_length=120, widget=input)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    reference_short_answer = forms.CharField(max_length=120, widget=input)


class CreateTaskWithDetailedAnswerForm(forms.Form):
    title = forms.CharField(max_length=120, widget=input)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
