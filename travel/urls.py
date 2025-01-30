from django.urls import path
from .views import CoolestDistrictsAPIView, TravelDecisionAPIView

urlpatterns = [
    path('coolest-districts/', CoolestDistrictsAPIView.as_view(), name='coolest_districts'),
    path('travel-decision/', TravelDecisionAPIView.as_view(), name='travel_decision'),
]