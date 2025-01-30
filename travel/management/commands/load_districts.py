from http import HTTPStatus
import requests
from django.core.management.base import BaseCommand
from travel.models import District

class Command(BaseCommand):
    help = 'Loads District data for all districts'

    def handle(self, *args, **options):
        url = 'https://raw.githubusercontent.com/strativ-dev/technical-screening-test/main/bd-districts.json'
        if District.objects.exists():
            District.objects.all().delete()
        response = requests.get(url)
        if response.status_code == HTTPStatus.OK.value:
            district_data = response.json()
            for data in district_data.get("districts", []):
                District.objects.create(
                    name=data.get("name", ""),
                    bn_name=data.get("bn_name", ""),
                    latitude=data.get("lat", 0),
                    longitude=data.get("long", 0),

                )

            self.stdout.write(self.style.SUCCESS('Successfully loaded Districts'))
        else:
            self.stdout.write(self.style.ERROR('Failed to load Districts'))
