from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='travel_users',  # Changed from user_set
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='travel_users',  # Changed from user_set
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

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