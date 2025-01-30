from django.core.management.base import BaseCommand
from travel.models import District, WeatherData
from travel.utils import fetch_weather_data

class Command(BaseCommand):
    help = 'Load weather data for all districts'
    def handle(self, *args, **options):
        districts = District.objects.all()
        for district in districts:
            self.stdout.write(f"Loading weather data for {district.name}....")
            if fetch_weather_data(district):
                self.stdout.write(self.style.SUCCESS(f'Successfully loaded weather data for {district.name}'))
            else:
                self.stdout.write(self.style.ERROR(f'Failed to load weather data for {district.name}'))
        self.stdout.write(self.style.SUCCESS('Successfully loaded weather data'))