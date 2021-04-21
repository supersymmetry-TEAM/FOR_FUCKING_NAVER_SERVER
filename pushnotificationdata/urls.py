
from django.urls import path
from .views import expotoken

app_name = "pushnotificationdata"

urlpatterns = [
path("expo-token",expotoken),
path("token",expotoken)
] 
