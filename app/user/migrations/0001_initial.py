# Generated by Django 4.0.3 on 2022-03-19 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('name', models.CharField(max_length=200, null=True)),
                ('describtion', models.TextField(blank=True, max_length=200, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_describtion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=500, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('teams', models.ManyToManyField(blank=True, to='user.team')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_manager', to='user.user_describtion'),
        ),
        migrations.AddField(
            model_name='team',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='team_users', to='user.user_describtion'),
        ),
    ]
