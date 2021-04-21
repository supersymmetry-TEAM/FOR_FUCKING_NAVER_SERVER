from rest_framework import viewsets, permissions
from recomments.serializer import RefoodcommentSerializer
from recomments.models import Refoodcomment

from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
  
class ReCommentViewSet(ModelViewSet):

    queryset = Refoodcomment.objects.all()
    serializer_class = RefoodcommentSerializer
    @action(detail=False, methods=["post"])
    def recomment_delete(self, request):
        pk = request.data.get('pk')
        comment_token = request.data.get("token")
        exist_id = self.queryset.get(pk=pk)
        if exist_id.token != comment_token:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            exist_id.delete()
            return Response(status=status.HTTP_200_OK)
    
    @action(detail=False, methods=["get"])
    def recomment_get_by_food(self, request):
        commentId = request.GET.get("comment_id", None)
        try:
            recos = Refoodcomment.objects.filter(comment__exact=commentId).order_by('created_date')
        except ValueError:
            return Response({"messege":"nodat"})
        serializer = RefoodcommentSerializer(recos, many=True, context={"request": request})
        return Response(serializer.data)