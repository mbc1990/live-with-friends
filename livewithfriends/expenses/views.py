from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView 
from expenses.models import House


def index(request):
    return HttpResponse("Hello world")

class HouseView(DetailView):
    template_name = "house.html"
    model = House

    def get_context_data(self, **kwargs):
        context = super(HouseView, self).get_context_data(**kwargs)
        context['test_var'] = 'hello context'
        return context
