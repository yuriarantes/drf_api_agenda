from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view

from core.models import Scheduling

@api_view(http_method_names=['GET'])
def scheduling_detail(request, id):
    """
    Search schdulings for id and return details
    """
    scheduling = get_object_or_404(Scheduling, id=id)


@api_view(http_method_names=['GET'])
def scheduling_list(request):
    """
    Search schdulings, return list
    """

