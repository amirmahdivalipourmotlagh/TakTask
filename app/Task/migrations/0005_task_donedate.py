# Generated by Django 4.0.3 on 2022-03-23 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0004_spenttime_related_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='donedate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
