from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views import View
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

        name = self.request.GET.get('name')
        if name != None:
            context['cars'] = Car.objects.filter(name__icontains=name)
        else:
            context['cars'] = Car.objects.all()
        return context
    
class CarCreate(CreateView):
    model = Car
    fields = ['name', 'price', 'img', 'description']
    template_name = 'car_create.html'
    success_url = '/cars/'