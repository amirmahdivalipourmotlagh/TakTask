from ctypes import Union
from distutils.command.build_scripts import first_line_re
from importlib.util import module_for_loader
from django.db import models
from django.contrib.auth.models import User
from  uuid import uuid4  
# Create your models here.



class User_describtion(models.Model):
    user=  models.OneToOneField(User,on_delete=models.CASCADE,null=False,blank=False)
    id  = models.UUIDField(default=uuid4,unique=True,primary_key=True,editable=False,null=False)
    username = models.CharField(max_length=200,null=False,blank=False,unique=True) 
    first_name = models.CharField(max_length=200,null=True,blank=True)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(max_length=500,null = True,blank = True)
    teams = models.ManyToManyField('Team',blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    # is_manager = models.BooleanField(default=False,null=False,blank=False,help_text='more accessable parts')
    def __str__(self):
        return self.username



class Team(models.Model):
    manager = models.ForeignKey(User_describtion,null=True,on_delete=models.SET_NULL,related_name='team_manager')
    users = models.ManyToManyField(User_describtion,blank=True,related_name='team_users')
    name = models.CharField(max_length=200,null=True)
    describtion = models.TextField(max_length=200,null=True,blank=True) 
    id = id  = models.UUIDField(default=uuid4,unique=True,primary_key=True,editable=False,null=False)
    create_time = models.DateTimeField(auto_now_add=True)
    # def __init__(self):
    #     for user in self.users:
    #         user.teams.add(Team.objects.get(id = self.id))
    
    def __str__ (self):
        return str(self.name)
        