from django.urls import path

from . import views

urlpatterns = [
    path("", views.AquariumSimulationView.as_view(), name="simulate_aquarium"),
]
