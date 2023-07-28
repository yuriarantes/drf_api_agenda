from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Scheduling
from .serializers import SchedulingSerializer

@api_view(http_method_names=['GET','PATCH','DELETE'])
def scheduling_detail(request, id):
    if request.method == "GET":
        """
        Search schdulings for id and return details
        """
        obj = get_object_or_404(Scheduling, id=id)

        serializer = SchedulingSerializer(obj)

        return JsonResponse(serializer.data)

    if request.method == "PATCH":
        """
        Update partial from schdulings for id and return details
        """
        obj = get_object_or_404(Scheduling, id=id)

        serializer = SchedulingSerializer(obj,data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=200, safe=False)
        
        return JsonResponse(serializer.errors, status=400)
    if request.method == "DELETE":
        """
        Remove schdulings for id
        """
        obj = get_object_or_404(Scheduling,id=id)
        obj.delete()

        return Response(status=204)


@api_view(http_method_names=['GET','POST'])
def scheduling_list(request):
    if request.method == "GET":
        """
        Search schdulings, return list of scheduling actives
        """
        qs = Scheduling.objects.filter(active=True)

        serializer = SchedulingSerializer(qs, many=True)

        return JsonResponse(serializer.data, safe=False)
    if request.method == "POST":
        """
        Create new schdulings, return detail
        """
        data = request.data

        serializer = SchedulingSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

