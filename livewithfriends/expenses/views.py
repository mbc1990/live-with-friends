import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, TemplateView

from expenses.models import House


def index(request):
    return HttpResponse("Hello world")

class DashboardView (TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['date'] = datetime.date.today()
        return context

    

class HouseView(DetailView):
    template_name = "house.html"
    model = House

    def get_context_data(self, **kwargs):
        context = super(HouseView, self).get_context_data(**kwargs)
        context['hello'] = 'hello context'
        return context
