from rest_framework import viewsets, permissions
from foodcomments.serializer import FoodCommentSerializer, WriteFoodCommentSerializer
from foodcomments.models import Foodcomment

from recomments.models import Refoodcomment
from recomments.serializer import RefoodcommentSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
  
class CommentViewSet(ModelViewSet):

    queryset = Foodcomment.objects.all()
    serializer_class = FoodCommentSerializer
    @action(detail=False, methods=["get"])
    def comment_notice_orderdtime(self, request):
        try:
            foods = Foodcomment.objects.filter(food__exact="공지사항").order_by('-created_date')
        except ValueErroe:
            return Response({"m":"No Data"})
        serializer = FoodCommentSerializer(foods, many=True, context ={"request": request})
        return Response(serializer.data)
    
    @action(detail=False, methods=["post"])
    def comment_post(self, request):
        pd_name = request.data.get('Food',None)
        comment_auth = request.data.get('Author',None)
        comment_text = request.data.get('Text',None)
        comment_token = request.data.get("Token",None)
        try:
            reco =Foodcomment(food=pd_name, text=comment_text, token=comment_token, author=comment_auth)
            reco.save()
            return Response(status=status.HTTP_200_OK)
        except ValueError:
            return Response({"messege":"Nodata"})

    @action(detail=False, methods=["post"])
    def comment_delete(self, request):
        pk = request.data.get('pk')
        comment_token = request.data.get("token")
        food = Foodcomment.objects.filter(id__exact=pk)[0]
        if food.token != comment_token:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            food.delete()
            return Response(status=status.HTTP_200_OK)
    @action(detail=False, methods=["get"])
    def comment_get_orderedtime(self, request):
        page = int(request.GET.get("page", None))
        start = (page-1)*10
        end = (page)*10
        try:
            foods = Foodcomment.objects.all().order_by('-created_date')[start:end]
        except ValueError:
            return Response({"messege":"nodat"})
        serializer = FoodCommentSerializer(foods, many=True,context={"request": request})
        return Response(serializer.data)    
    @action(detail=False, methods=["get"])
    def comment_get_by_food(self, request):
        food = request.GET.get("food", None)
        try:
            foods = Foodcomment.objects.filter(food__exact=food).order_by('-created_date')
        except ValueError:
            return Response({"messege":"nodat"})
        serializer = FoodCommentSerializer(foods, many=True,context={"request": request})
        return Response(serializer.data)
    @action(detail=False, methods=["get"])
    def recomment_get_by_comment(self, request):
        commentId = request.GET.get("comment_id", None)
        # get recomments using comment id
        try:
            co = Foodcomment.objects.get(pk=commentId)
        # ReFoodComment from object co one can get set of one two many field by small(ReFoodComment)_set.all()
            recos = co.refoodcomment_set.all().order_by('-created_date')
        except ValueError:
            return Response({"messege":"nodat"})
        serializer = RefoodcommentSerializer(recos, many=True,context={"request": request})
        return Response(serializer.data)
    @action(detail=False, methods=["post"])
    def recomment_post_by_comment(self, request):
        
        commentId = int(request.data.get("comment_id", None))
        commentText = request.data.get("comment_text", None)
        authToken = request.data.get("auth_token", None)
        auth = request.data.get("author", None)
        # get recomments using comment id
        try:
            co = Foodcomment.objects.filter(id__exact=commentId)
        # from object co one can get set of one two many field by small(ReFoodComment)_set.all()
            reco = Refoodcomment(foodcomment=co[0], text=commentText, token=authToken, author=auth)
            reco.save()
            return Response(status=status.HTTP_200_OK)
        except ValueError:
            return Response({"messege":"What the hell!"})

        
    @action(detail=False, methods=["post"])
    def comment_up(self, request):
        commentId = request.data.get("comment_id", None)
        authId = str(request.data.get("auth_id", None))
        up = request.data.get("up_num", None)

        # get recomments using comment id
        try:
            co = Foodcomment.objects.filter(id__exact=commentId)
            upset = set(str(co[0].is_up_list).split(","))
            if authId in upset:
                upset.remove(authId)
                st = ""
                for ele in upset:
                    st +=ele+","
                co.update(is_up_list=st,up=up-1)
            else:
                st = co[0].is_up_list+authId+","   
                co.update(is_up_list=st,up=up+1)
        except ValueError:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_200_OK)
    @action(detail=False, methods=["post"])
    def comment_down(self, request):
        commentId = request.data.get("comment_id", None)
        authId = str(request.data.get("auth_id", None))
        down = request.data.get("down_num", None)
        # get recomments using comment id
        try:
            co = Foodcomment.objects.filter(id__exact=commentId)
            downset = set(str(co[0].is_down_list).split(","))
            if authId in downset:
                downset.remove(authId)
                st = ""
                for ele in downset:
                    st +=ele+","
                co.update(is_down_list=st,down=down-1)
            else:
                st = co[0].is_down_list+authId+","   
                co.update(is_down_list=st,down=down+1)
        except ValueError:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_200_OK)
    @action(detail=False, methods=["post"])
    def recomment_delete(self, request):
        pk = request.data.get('pk')
        comment_token = request.data.get("token")
        food = Refoodcomment.objects.filter(id__exact=pk)[0]
        if food.token != comment_token:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            food.delete()
            return Response(status=status.HTTP_200_OK)