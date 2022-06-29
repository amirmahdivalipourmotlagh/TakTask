from asyncio import Task
from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(task)
admin.site.register(SpentTime)