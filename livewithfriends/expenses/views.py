from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from expenses.models import House


def index(request):
    return HttpResponse("Hello world")

class HouseView(TemplateView):
    template_name = "house.html"

    def get_context_data(self, **kwargs):
        context = super(HouseView, self).get_context_data(**kwargs)
        context['house_name'] = House.objects.first().name
        return context
