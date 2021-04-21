from django.db import models
from datetime import timezone
class Foodcomment(models.Model):
    food = models.CharField(max_length=300)
    token = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    up = models.IntegerField(default=0)
    down = models.IntegerField(default=0)
    is_up_list = models.TextField(default="")
    is_down_list = models.TextField(default="")

