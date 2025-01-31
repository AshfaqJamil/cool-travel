from django.urls import path
from .views import CoolestDistrictsAPIView, TravelDecisionAPIView, RegisterView
from .views import LoginView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('coolest-districts/', CoolestDistrictsAPIView.as_view(), name='coolest_districts'),
    path('travel-decision/', TravelDecisionAPIView.as_view(), name='travel_decision'),
]