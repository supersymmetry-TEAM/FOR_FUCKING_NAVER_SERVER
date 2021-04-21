from django.urls import path
from foodcomments.views import  CommentViewSet
from rest_framework.routers import DefaultRouter
app_name = "foodcomments"
router = DefaultRouter()
router.register("", CommentViewSet)
urlpatterns = router.urls

