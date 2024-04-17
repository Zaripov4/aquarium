from django.views.generic import TemplateView
from django.shortcuts import render
from .aquarium import Aquarium

class AquariumSimulationView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        aquarium = Aquarium()
        aquarium.populate_aquarium()
        output = aquarium.start_simulation()
        context["output"] = output
        return context
