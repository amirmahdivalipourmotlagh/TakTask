# Generated by Django 4.0.3 on 2022-03-25 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0009_remove_spenttime_related_team_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spenttime',
            name='related_task',
        ),
    ]
