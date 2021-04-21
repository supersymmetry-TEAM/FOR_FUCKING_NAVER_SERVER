from django.db import models
from foodcomments.models import Foodcomment
class Refoodcomment(models.Model):
    token = models.CharField(max_length=500)
    foodcomment = models.ForeignKey(Foodcomment,on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=500)
    up = models.IntegerField(default=0)
    down = models.IntegerField(default=0)
    is_up_list = models.TextField(default=",")
    is_down_list = models.TextField(default=",")
