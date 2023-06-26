from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Car

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

class CarsList(TemplateView):
    template_name = 'cars_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        model = self.request.GET.get('model')
        if model != None:
            context['cars'] = Car.objects.filter(name__icontains=model)
        else:
            context['cars'] = Car.objects.all()
        return context