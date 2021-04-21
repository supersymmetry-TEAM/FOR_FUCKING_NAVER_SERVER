from django.urls import path
from recomments.views import  ReCommentViewSet
from rest_framework.routers import DefaultRouter
app_name = "recomments"
router = DefaultRouter()
router.register("", ReCommentViewSet)
urlpatterns = router.urls

