from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Scheduling, Schedule, Store
from .serializers import SchedulingSerializer

from datetime import datetime, timedelta

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

@api_view(http_method_names=['GET'])
def schedule_list(request):
    schedules = []

    store_id = request.query_params.get('store')
    date = datetime.strptime(request.query_params.get('date'),'%Y-%m-%d').date()

    obj_schedule = Schedule.objects.filter(store=store_id,day=date.weekday()).first()

    time = obj_schedule.first_start_at
    first_end_at = obj_schedule.first_end_at

    if obj_schedule.last_end_at:
        last_time = obj_schedule.last_end_at
    else:
        last_time = obj_schedule.first_end_at

    while time < last_time:
        if obj_schedule.last_start_at:
            if time >= obj_schedule.first_end_at and time < obj_schedule.last_start_at:
                ...
        schedules.append(time)

    
        time = (datetime.combine(datetime.today(), time) + timedelta(minutes=30)).time()
        

    print(obj_schedule.first_start_at)
    print(obj_schedule.last_start_at)


    dict = {
        "store": store_id,
        "date": date,
        "times":schedules,
    }

    return JsonResponse(dict)

