from django.db import models
from datetime import timezone
class ExpoPushToken(models.Model):
    expotoken = models.CharField(max_length=100)
    userId = models.CharField(max_length=50)
    
class SendHistory(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    number_of_users = models.CharField(max_length=50,default='NO')
    message = models.CharField(max_length=500,default='NO')
    title = models.CharField(max_length=200,default='NO')
# Create your models here.
