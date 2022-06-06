from django.db import models
from django.contrib.auth.models import User
from project.models import Project

# Create your models here.
class Log(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, to_field='id')
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, to_field='id')
    duration = models.FloatField()
    remarks = models.CharField(max_length=200, null=True)
    date = models.DateField()
    is_late = models.BooleanField(null=True)

 

