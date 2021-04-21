from rest_framework.permissions import BasePermission
from foodcomments.models import Foodcomment
class IsSelf(BasePermission):
    def has_object_permission(self, request, view, user):
        token = request.data.get("token", None)
        
        if token is not None:
            
            return
        return bool(user == request.user)