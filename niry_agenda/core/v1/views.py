from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Scheduling, Schedule, Store
from .serializers import SchedulingSerializer

from datetime import datetime, timedelta

from .services import SchedulesServices


class SchedulingDetail(APIView):
    def get(self,request, id):
        """
        Search schdulings for id and return details
        """
        obj = get_object_or_404(Scheduling, id=id)

        serializer = SchedulingSerializer(obj)

        return JsonResponse(serializer.data)

    def patch(self,request,id):
        """
        Update partial from schdulings for id and return details
        """
        obj = get_object_or_404(Scheduling, id=id)

        serializer = SchedulingSerializer(obj,data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=200, safe=False)
        
        return JsonResponse(serializer.errors, status=400)

    def delete(self,request,id):
        """
        Remove schdulings for id
        """
        obj = get_object_or_404(Scheduling,id=id)
        obj.delete()

        return Response(status=204)

class SchedulingList(APIView):
    def get(self, request):
        """
        Search schdulings, return list of scheduling actives
        """
        qs = Scheduling.objects.filter(active=True)

        serializer = SchedulingSerializer(qs, many=True)

        return JsonResponse(serializer.data, safe=False)

    def post(self,request):
        """
        Create new schdulings, return detail
        """
        try:
            data = request.data

            store = data['store']
            scheduling_datetime = datetime.strptime(data['scheduling_date'], '%Y-%m-%dT%H:%M:%SZ')
            scheduling_date = scheduling_datetime.date()
            scheduling_time = scheduling_datetime.time()

            schedules = SchedulesServices.get_available_times(store,scheduling_date)

            if scheduling_time in schedules:
                serializer = SchedulingSerializer(data=data)

                if serializer.is_valid():
                    serializer.save()

                    return JsonResponse(serializer.data, status=201)

                return JsonResponse(serializer.errors, status=400)
            
            return JsonResponse({"error":"The specified time is not available."})
        except Exception as error:
            return JsonResponse({"error":str(error)}, status=500) 

class ScheduleList(APIView):
    def get(self, request):
        store_id = request.query_params.get('store')
        date = datetime.strptime(request.query_params.get('date'),'%Y-%m-%d').date()

        schedules = SchedulesServices.get_available_times(store_id,date)

        dict = {
            "store": store_id,
            "date": date,
            "times":schedules,
        }

        return JsonResponse(dict)