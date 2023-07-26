from django.db import models

class Scheduling(models.Model):
    scheduling_date = models.DateTimeField()
    name = models.CharField(max_length=240)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    active = models.BooleanField(null=True)