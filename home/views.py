from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from .forms import UserForm
from .models import Innovation, Activities, Announcement

class IndexView(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Announcement.objects.all()


class InnovationView(generic.ListView):
    template_name = 'home/innovation.html'
    context_object_name = 'all_inn'

    def get_queryset(self):
        return Innovation.objects.all()

class DetailView(generic.DetailView):
    model=Innovation
    template_name = 'home/detail.html'

class ActivityView(generic.ListView):
    template_name = 'home/innovation.html'
    context_object_name = 'all_act'

    def get_queryset(self):
        return Activities.objects.all()

class InnovationCreate(CreateView):
    model = Innovation
    fields = ['innovator', 'title', 'brief','image', 'detail', 'file' ]

class InnovationUpdate(UpdateView):
    model = Innovation
    fields = ['innovator', 'title', 'brief', 'image', 'detail', 'file']
    template_name= 'home/update_form.html'
    def get(self,request,**kwargs):
        self.object=Innovation.objects.get(id=self.request.id)
        from_class=self.get_form(form_class='home/update_form.html')

class InnovationDelete(DeleteView):
    model = Innovation
    fields = ['innovator', 'title', 'brief', 'image', 'detail', 'file']
