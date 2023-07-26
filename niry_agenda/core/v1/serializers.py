from rest_framework import serializers
from ..models import Scheduling

class SchedulingSerializer(serializers.Serializer):
    scheduling_date = serializers.DateTimeField()
    name = serializers.CharField(max_length=240)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=15)
    active = serializers.BooleanField(allow_null=True)
    