from rest_framework import serializers
from models import Scheduling

class SchedulingSerializer(serializers.Serializer):
    model = Scheduling
    fields = ['scheduling_date','name','email','phone']

    