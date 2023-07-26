from rest_framework import serializers
from ..models import Scheduling

class SchedulingSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    scheduling_date = serializers.DateTimeField()
    name = serializers.CharField(max_length=240)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=15)
    active = serializers.BooleanField(allow_null=True)
    
    def create(self, validated_data):
        scheduling = Scheduling.objects.create(
            scheduling_date = validated_data['scheduling_date'],
            name = validated_data['name'],
            email = validated_data['email'],
            phone = validated_data['phone'],
            active = validated_data['active'],
        )

        return scheduling
    
    def update(self, instance, validated_data):
        instance.scheduling_date = validated_data.get('scheduling_date', instance.scheduling_date)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.active = validated_data.get('active', instance.active)
        instance.save()

        return instance