from django.db import models

class Store(models.Model):
    social_name = models.CharField(max_length=240, unique=True)
    cnpj = models.CharField(max_length=14)
    active = models.BooleanField(null=True)

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

    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    day = models.CharField(max_length=20, choices=DAY_CHOICES)
    first_start_at = models.TimeField()
    first_end_at = models.TimeField()
    last_start_at = models.TimeField(null=True, blank=True)
    last_end_at = models.TimeField(null=True, blank=True)

class Scheduling(models.Model):
    scheduling_date = models.DateTimeField()
    name = models.CharField(max_length=240, unique=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    active = models.BooleanField(null=True)

    def __str__(self) -> str:
        return self.name



