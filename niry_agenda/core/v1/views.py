from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view

from ..models import Scheduling
from .serializers import SchedulingSerializer

@api_view(http_method_names=['GET','PUT','PATCH'])
def scheduling_detail(request, id):
    if request.method == "GET":
        """
        Search schdulings for id and return details
        """
        obj = get_object_or_404(Scheduling, id=id)

        serializer = SchedulingSerializer(obj)

        return JsonResponse(serializer.data)

    if request.method == "PUT":
        obj = get_object_or_404(Scheduling, id=id)

        serializer = SchedulingSerializer(data=request.data)

        if serializer.is_valid():
            v_data = serializer.validated_data

            obj.scheduling_date = v_data.get('scheduling_date', obj.scheduling_date)
            obj.name = v_data.get('name', obj.name)
            obj.email = v_data.get('email', obj.email)
            obj.phone = v_data.get('phone', obj.phone)
            obj.active = v_data.get('active', obj.active)

            obj.save()

            new_serializer = SchedulingSerializer(get_object_or_404(Scheduling, id=id))

            new_data = new_serializer.data

            return JsonResponse(new_data, status=204, safe=False)
        
        return JsonResponse(serializer.errors, status=400)

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
        """
        Create new schdulings, return detail
        """
        data = request.data

        serializer = SchedulingSerializer(data=data)

        if serializer.is_valid():
            validated_data = serializer.validated_data

            Scheduling.objects.create(
                scheduling_date = validated_data['scheduling_date'],
                name = validated_data['name'],
                email = validated_data['email'],
                phone = validated_data['phone'],
                active = validated_data['active'],
            )

            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

