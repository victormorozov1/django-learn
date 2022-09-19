from django.db import models
from django.contrib.auth.models import User
from time import gmtime, strftime
# Посмотреть про удаление!


class TaskModel(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    likes = models.IntegerField(default=0)
    detail_answer = models.BooleanField(default=True, null=True)  # detailed_answer or short_answer
    reference_short_answer = models.TextField(blank=True)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Task {self.title}: {self.description[:20:]}'


class Answer(models.Model):
    text = models.TextField()
    status = models.CharField(max_length=20, null=True)  # Approved / Rejected / Waiting for check
    make_public_responding_user = models.BooleanField(default=False, null=True)
    make_public_task_admin = models.BooleanField(default=False, null=True)
    responding_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    task = models.ForeignKey(TaskModel, on_delete=models.CASCADE)
