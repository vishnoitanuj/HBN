from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from .forms import UserForm
from .models import Innovation, Activities, Announcement
from django.db.models import Q

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
    template_name = 'home/activities.html'
    context_object_name = 'all_act'

    def get_queryset(self):
        return Activities.objects.all()


class InnovationCreate(CreateView):
    model = Innovation
    fields = ['innovator', 'title', 'brief','image', 'detail', 'file' ]

class InnovationUpdate(UpdateView):
    model = Innovation
    fields = ['innovator', 'title', 'brief', 'image', 'detail', 'file']
    template_name_suffix = '_update_form'

class InnovationDelete(DeleteView):
    model = Innovation
    fields = ['innovator', 'title', 'brief', 'image', 'detail', 'file']

class InnovationSearch(generic.ListView):
    paginate_by = 10

    def get_queryset(self):
        result = super(InnovationSearch, self).get_queryset()

        query = self.request.GET.get('q')
        if(query):
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(content__icontains=q) for q in query_list))
            )

        return result
