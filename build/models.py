import datetime
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

class personaldet(models.Model):
    email = models.EmailField()
    graduateyear = models.CharField(max_length=255)
    percentage= models.IntegerField()
    yearofgraduation = models.DateField(blank=True, null=True,default=datetime.date.today)
    skills = models.CharField(max_length=255)
    interested_sub = models.CharField(max_length=255)
    date= models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    

