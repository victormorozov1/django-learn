# Generated by Django 4.1.1 on 2022-09-19 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_alter_taskmodel_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
