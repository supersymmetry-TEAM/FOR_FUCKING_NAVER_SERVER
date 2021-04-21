from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from .serializers import NutDataSerializer_1
from .models import NutData_1
class OwnPagination(PageNumberPagination):
    page_size = 20
@api_view(["GET"])
def nut_search(request):
    paginator = OwnPagination()
    pd_name = request.GET.get("pd_name", None)
    pd_name_nospace = pd_name.replace(" ","")
    filter_kwargs = {}
    if pd_name is not None:
        filter_kwargs["PROD_NAME__icontains"] = pd_name
    try:
        foods = NutData_1.objects.filter(**filter_kwargs).order_by('SEARCH_SCORE','-PROD_NAME')
    except ValueError:
        foods = NutData_1.objects.all()
    results = paginator.paginate_queryset(foods, request)
    serializer = NutDataSerializer_1(results, many=True,context={"request": request})
    return paginator.get_paginated_response(serializer.data)
# Create your views here.
