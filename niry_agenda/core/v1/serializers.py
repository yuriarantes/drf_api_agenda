from rest_framework import serializers
from django.utils import timezone
from datetime import date

import logging

from ..models import Scheduling

logging.basicConfig(level=logging.DEBUG,
                    filename='app.log',
                    format='%(asctime)s - %(levelname)s - %(message)s')

class SchedulingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheduling
        fields = ['id','scheduling_date','name','email','phone','active']

    extra_kwargs= {
        'name': {'unique': True}
    }

    def validate(self, attrs):
        email_request = attrs.get("email","")
        phone_request = attrs.get("phone","")
        date_request = attrs.get("scheduling_date","")
        if email_request.endswith(".br") and phone_request.startswith("+") and not phone_request.startswith("+55"):
            message_error = "Brazilian email must be associated with a brazilian phone number (+55)"
            logging.error(message_error)
            raise serializers.ValidationError(message_error)

        if Scheduling.objects.filter(email=email_request, scheduling_date__date=date_request.date()):
            message_error = "There are already schedulings for this email and appointment day"
            logging.error(message_error)
            raise serializers.ValidationError(message_error)
        
        return attrs

    def validate_scheduling_date(self, value):
        if value < timezone.now():
            message_error = "Scheduling can't created in the past"
            logging.error(message_error)
            raise serializers.ValidationError(message_error)
            
        return value
    
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

