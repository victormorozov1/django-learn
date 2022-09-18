from django.db import models
from django.contrib.auth.models import User

# Посмотреть про удаление!


class Task(models.Model):
    title = models.CharField(max_length=120, default='Task')
    description = models.TextField()
    likes = models.IntegerField(default=0)
    detail_answer = models.BooleanField(default=True, null=True)  # detailed_answer or short_answer
    reference_short_answer = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Task {self.title}: {self.description[:20:]}'


class DetailedAnswer(models.Model):
    text = models.TextField()
    responding_user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
