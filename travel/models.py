from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class District(models.Model):
    name = models.CharField(max_length=100)
    bn_name = models.CharField(max_length=100)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name


class WeatherData(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='weather_data')
    date = models.DateField(null=True, blank=True)
    temperature_at_2pm = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.district.name} - {self.date} - {self.temperature_at_2pm}"