# Generated by Django 4.1.1 on 2022-09-19 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_taskmodel_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskmodel',
            name='status',
        ),
        migrations.AddField(
            model_name='answer',
            name='status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
