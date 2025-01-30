from django.contrib import admin
from .models import District, WeatherData, User
# Register your models here.
admin.site.register(District)
admin.site.register(WeatherData)
admin.site.register(User)