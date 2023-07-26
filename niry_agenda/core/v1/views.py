from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view

from ..models import Scheduling
from .serializers import SchedulingSerializer

@api_view(http_method_names=['GET'])
def scheduling_detail(request, id):
    """
    Search schdulings for id and return details
    """
    obj = get_object_or_404(Scheduling, id=id)

    serializer = SchedulingSerializer(obj)

    if serializer.is_valid():
        return JsonResponse(serializer.data)
    else:
        return JsonResponse(serializer.errors)


@api_view(http_method_names=['GET'])
def scheduling_list(request):
    """
    Search schdulings, return list
    """

