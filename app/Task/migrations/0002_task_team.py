# Generated by Django 4.0.3 on 2022-03-19 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.team'),
        ),
    ]