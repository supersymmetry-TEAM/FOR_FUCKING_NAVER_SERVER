from django.shortcuts import render
from .models import ExpoPushToken
from .serializers import ExpoPushTokenSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
 

@api_view(["GET","POST"])
def expotoken(request):
    if request.method == "POST":
        etoken = request.data.get('expoPushToken',None)
        uId = request.data.get('userId', None)
        if ExpoPushToken.objects.filter(expotoken__exact=etoken):
            return Response(status=status.HTTP_200_OK)
        try:
            reco = ExpoPushToken(expotoken=etoken, userId=uId)
            reco.save()
            return Response(status=status.HTTP_200_OK)
        except ValueError:
            return Response({"messege":"Nodata"})
    tokens = ExpoPushToken.objects.all()
    serializer = ExpoPushTokenSerializer(tokens, many=True, context={"request": request})
    return Response(serializer.data)

