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

    return JsonResponse(serializer.data)


@api_view(http_method_names=['GET','POST'])
def scheduling_list(request):
    if request.method == "GET":
        """
        Search schdulings, return list
        """
        qs = Scheduling.objects.all()

        serializer = SchedulingSerializer(qs, many=True)

        return JsonResponse(serializer.data, safe=False)
    if request.method == "POST":
        data = request.data

        serializer = SchedulingSerializer(data=data)

        if serializer.is_valid():
            validated_data = serializer.data

            Scheduling.objects.create(
                scheduling_date = validated_data['scheduling_date'],
                name = validated_data['name'],
                email = validated_data['email'],
                phone = validated_data['phone'],
                active = validated_data['active'],
            )

            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

