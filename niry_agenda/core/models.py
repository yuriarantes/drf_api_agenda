from django.db import models
from multiselectfield import MultiSelectField

import uuid

class Client(models.Model):
    name = models.CharField(max_length=240, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)

    def __str__(self) -> str:
        return self.name

class Store(models.Model):
    social_name = models.CharField(max_length=240)
    cnpj = models.CharField(max_length=14, unique=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.social_name

class Schedule(models.Model):
    DAY_CHOICES = (
        ('0','Monday'),
        ('1','Tuesday'),
        ('2','Wednesday'),
        ('3','Thursday'),
        ('4','Friday'),
        ('5','Saturday'),
        ('6','Sunday'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    store = models.ForeignKey(Store, related_name="schedules", on_delete=models.CASCADE)
    day = MultiSelectField(choices=DAY_CHOICES)
    first_start_at = models.TimeField()
    first_end_at = models.TimeField()
    last_start_at = models.TimeField(null=True, blank=True)
    last_end_at = models.TimeField(null=True, blank=True)

class Scheduling(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    scheduling_date = models.DateTimeField()
    store = models.ForeignKey(Store, related_name="scheduling", on_delete=models.CASCADE, null=False)
    client  = models.ForeignKey(Client, related_name="scheduling", on_delete=models.CASCADE,null=False)
    active = models.BooleanField(null=False, default=True)
    
    def __str__(self) -> str:
        return self.name