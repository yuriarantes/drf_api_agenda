from rest_framework import serializers
from django.utils import timezone
from datetime import date, timedelta

import logging

from ..models import Scheduling, Client, Schedule

logging.basicConfig(level=logging.DEBUG,
                    filename='app.log',
                    format='%(asctime)s - %(levelname)s - %(message)s')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id','name','email','phone']
    
    extra_kwargs= {
        'name': {'unique': True}
    }

    def validate_phone(self, value):   
        if len(value) < 8:
            message_error = "Phone number cannot be less than 8 characters"
            logging.error(message_error)
            raise serializers.ValidationError(message_error)

        if value.startswith("+"):
            new_value = value[1:]

            if not new_value.isdigit():
                raise serializers.ValidationError("Phone cannot contain special characters")

        return value

    def validate(self, attrs):
        email_request = attrs.get("email","")
        phone_request = attrs.get("phone","")

        if email_request.endswith(".br") and phone_request.startswith("+") and not phone_request.startswith("+55"):
            message_error = "Brazilian email must be associated with a brazilian phone number (+55)"
            logging.error(message_error)
            raise serializers.ValidationError(message_error)


class SchedulingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheduling
        fields = ['id','scheduling_date','store','client','active']
    
    extra_kwargs= {
        'active': {'write_only': False}
    }

    def validate(self, attrs):
        client = attrs.get("client","")
        date_request = attrs.get("scheduling_date","")
 
        if Scheduling.objects.filter(client=client, scheduling_date__date=date_request.date()):
            message_error = "There are already schedulings for this client and appointment day"
            logging.error(message_error)
            raise serializers.ValidationError(message_error)
        
        if Scheduling.objects.filter(scheduling_date__gte=date_request-timedelta(minutes=30), scheduling_date__lte=date_request+timedelta(minutes=30)):
            message_error = "There are schedules within 30 minutes before or after"
            logging.error(message_error)
            raise serializers.ValidationError(message_error)
        
        return attrs

    def validate_scheduling_date(self, value):
        if value < timezone.now():
            message_error = "Scheduling can't created in the past"
            logging.error(message_error)
            raise serializers.ValidationError(message_error)
            
        return value
    
class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id','store','day','first_start_at','first_end_at','last_start_at','last_end_at']