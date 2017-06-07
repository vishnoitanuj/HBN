from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from .models import Innovation, Activities, Announcement, NetworkMember, Suggestion
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect,HttpResponseRedirect,get_object_or_404
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import login,logout, get_user_model,authenticate
from .forms import InnovationForm
from django.contrib import messages

class IndexView(generic.ListView):
    model = Suggestion
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

class ActivityDetail(generic.DetailView):
    model = Activities
    template_name = 'home/activity_detail.html'

# class InnovationCreate(CreateView):
#     model = Innovation
#     fields = ['innovator', 'title','location','image', 'detail', 'file' ]

def innovation_create(request):
    form = InnovationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request,"home/innovation_form.html", context)


def innovation_update(request, pk=None):
    instance = get_object_or_404(Innovation,pk=pk)
    form = InnovationForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title":instance.title,
        "instance":instance,
        "form": form,
    }
    return render(request, "home/innovation_form.html", context)


def innovation_delete(request, pk=None):
    instance = get_object_or_404(Innovation, pk=pk)
    instance.delete()
    messages.success(request,"Successfully Deleted")
    return redirect("home:innovation")



# class InnovationUpdate(UpdateView):
#     model = Innovation
#     fields = ['innovator', 'title', 'location','image', 'detail', 'file']
#     template_name_suffix = '_update_form'
#
# class InnovationDelete(DeleteView):
#     model = Innovation
#     fields = ['innovator', 'title','location', 'image', 'detail', 'file']


class ActivityView(generic.ListView):
    template_name = 'home/activities.html'
    context_object_name = 'all_act'

    def get_queryset(self):
        return Activities.objects.all()

class AboutView(generic.ListView):
    template_name = 'home/about.html'
    context_object_name = 'all_mem'

    def get_queryset(self):
        return NetworkMember.objects.all()

#
# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()  # load the profile instance created by the signal
#             user.profile.birth_date = form.cleaned_data.get('birth_date')
#             user.save()
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=user.username, password=raw_password)
#             login(request, user)
#             return redirect('index')
#     else:
#         form = SignUpForm()
#     return render(request, 'home/signup.html', {'form': form})


def login_view(request):
    print(request.user.is_authenticated())
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username  = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request,user)
        print(request.user.is_authenticated())
        #redirect
        return redirect("/home")
    return render(request, "home/form.html", {"form":form,"title":title})

def logout_view(request):
    logout(request)
    return redirect("/home")

User = get_user_model()
def register_view(request):
    print(request.user.is_authenticated())
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user=form.save(commit=False)
        password=form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("/home")

    context = {
        "form": form,
        "title": title
    }
    return render(request, "home/form.html", context)

