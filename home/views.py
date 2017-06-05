from django.views import generic
import operator
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from .forms import UserForm
from .models import Innovation, Activities, Announcement
from django.db.models import Q
import functools
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Announcement.objects.all()


# class InnovationView(generic.ListView):
#     model = Innovation
#     template_name = 'home/innovation.html'
#     context_object_name = 'all_inn'
#     paginate_by = 6
#
#     def get_queryset(self):
#         result  = super(InnovationView,self).get_queryset()
#
#         query = self.request.GET.get('q')
#         if query:
#             query_list = query.split()
#             result = result.filter(
#                 reduce(operator.and_,
#                        (Q(title__icontains=q) for q in query_list)) |
#                 reduce(operator.and_,
#                        (Q(detail__icontains=q) for q in query_list))
#             )
#
#         return result


def innovation_list(request):
    today = timezone.now().date()
    queryset_list = Innovation.objects.all()

    queryset_list = Innovation.objects.all()

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(detail__icontains=query) |
            Q(innovator__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, 6)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "title": "List",
        "page_request_var": page_request_var,
        "today": today,
    }
    return render(request, "home/innovation.html", context)


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
    template_name_suffix = '_update_form'

class InnovationDelete(DeleteView):
    model = Innovation
    fields = ['innovator', 'title', 'brief', 'image', 'detail', 'file']
