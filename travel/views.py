from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import District, WeatherData
from django.http import JsonResponse

def root_view(request):
    return JsonResponse({
        'message': 'Welcome to the Cool Travel API!',
        'endpoints': {
            'coolest_districts': '/api/coolest-districts/',
            'travel_decision': '/api/travel-decision/?source=SOURCE&destination=DESTINATION&date=YYYY-MM-DD'
        }
    })
class CoolestDistrictsAPIView(APIView):
    def get(self, request):
        districts = District.objects.all()
        district_temps = []
        for district in districts:
            temps = WeatherData.objects.filter(district=district).values_list("temperature_at_2pm", flat=True)
            avg_temp = sum(temps) / 7
            district_temps.append({"district": district.name, "average_temperature": round(avg_temp, 3)})

        coolest_districts = sorted(district_temps, key=lambda x: x["average_temperature"], reverse=True)[:10]
        return Response(coolest_districts)

class TravelDecisionAPIView(APIView):
    def get(self, request):
        source = request.GET.get("source")
        destination = request.GET.get("destination")
        date = request.GET.get("date")

        if not all([source, destination, date]):
            return Response({"error": "Missing parameters"}, status.HTTP_400_BAD_REQUEST)
        try:
            source_district = District.objects.get(name=source.title())
            destination_district = District.objects.get(name=destination.title())
        except District.DoesNotExist:
            return Response({"error": "Invalid district name"}, status.HTTP_404_NOT_FOUND)

        try:
            source_tem = WeatherData.objects.get(district=source_district, date=date).temperature_at_2pm
            destination_tem = WeatherData.objects.get(district=destination_district, date=date).temperature_at_2pm

        except WeatherData.DoesNotExist:
            return Response({"error": "Weather data not available for given date"}, status.HTTP_404_NOT_FOUND)

        decision = f"Yes, you may travel to {destination_district.name}" if source_tem > destination_tem else f"No, you should stay in {source_district.name}"
        return Response(
            {
                "source_temperature": source_tem,
                "destination_temperature": destination_tem,
                "decision": decision,
                },
            status = status.HTTP_200_OK
        )