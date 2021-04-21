
from django.urls import path
from .views import nut_search
app_name = "nutdata"

urlpatterns = [
    path("search_nut/", nut_search),
  ]
