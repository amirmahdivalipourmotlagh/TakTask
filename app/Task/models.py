from email.errors import InvalidMultipartContentTransferEncodingDefect
from email.policy import default
from xml.parsers.expat import model
from django.db import models
from uuid import uuid4
from user.models import Team, User_describtion
import datetime
# Create your models here.


class task(models.Model):
    id  = models.UUIDField(default=uuid4,unique=True,primary_key=True,editable=False,null=False)
    title = models.CharField(max_length=200,blank=True)
    user=  models.ForeignKey(User_describtion,on_delete=models.CASCADE,blank=False)
    team = models.ForeignKey(Team,on_delete=models.CASCADE,blank=True,null=True)
    create_time = models.DateField(auto_now_add=True)
    DueDate = models.DateField(null=True,name='duedate',blank=True)
    estimate_time = models.IntegerField(default=None,null=True,blank=True)
    time_spented_up = models.ManyToManyField('SpentTime',blank=True,related_name='time_spended')
    If_Done = models.BooleanField(default=False,blank=False)
    Done_time = models.DateField(default=None,null=True,blank=True)
    orginal_done = False
    def __str__(self):
        return str(self.title + "__{ " + self.user.username + " }__" + str(self.id))


class SpentTime(models.Model):
    id = models.UUIDField(default=uuid4,unique=True,primary_key=True,editable=False,null=False)
    start_date = models.DateField(default=None,null=True,blank=True)
    start_time = models.TimeField(auto_now_add=True,null=True,blank=True)
    spended = models.IntegerField(default=0,null = True,blank=False)
    related_task = models.ForeignKey(task,on_delete=models.CASCADE,blank=True,null=True)
    related_user = models.ForeignKey(User_describtion,on_delete=models.CASCADE,blank=True,null=True,default=None)
    related_team = models.ForeignKey(Team,on_delete=models.CASCADE,blank=True,null=True,default=None)
    def __str__(self):
        return str(self.id)

     