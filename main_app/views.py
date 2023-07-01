from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
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

    def get_success_url(self):
        return reverse('car_detail', kwargs={'pk': self.object.pk})

class CarDetail(DetailView):
    model = Car
    template_name = 'car_detail.html'


class CarUpdate(UpdateView):
    model = Car
    fields = ['name', 'price', 'img', 'description']
    template_name = 'car_update.html'
    success_url = '/cars/'
    
    def get_success_url(self):
        return reverse('car_detail', kwargs={'pk': self.object.pk})
    
class CarDelete(DeleteView):
    model = Car
    template_name = 'car_delete_confirmation.html'
    success_url = '/cars/'