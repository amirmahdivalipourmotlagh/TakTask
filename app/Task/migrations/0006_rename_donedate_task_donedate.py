# Generated by Django 4.0.3 on 2022-03-23 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0005_task_donedate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='donedate',
            new_name='DoneDate',
        ),
    ]
