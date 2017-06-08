from django.conf.urls import url
from .import views
from django.views.generic.dates import ArchiveIndexView
from home.models import Innovation
from .import views as core_views
from django.contrib.auth import views as auth_views
from .views import logout_view,register_view,login_view


app_name='home'
urlpatterns = [
    #/home/
    url(r'^$', views.index_view, name='index'),
    url(r'innovation/$' , views.innovation_list, name='innovation' ),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/detail$', views.DayDetailView.as_view(), name='day-detail'),
    url(r'(?P<pk>[0-9]+)/activities/$', views.ActivityDetail.as_view(), name='act-detail'),
    url(r'activities/$', views.ActivityView.as_view(), name='activities'),



    #home/innovation/addInnovation
    url(r'innovation/add/$', views.innovation_create, name='inn-add'),
    url(r'(?P<pk>[0-9]+)/edit/$', views.innovation_update, name='inn-update'),
    url(r'(?P<pk>[0-9]+)/delete/$', views.innovation_delete, name='inn-delete'),
    url(r'about/',views.AboutView.as_view(), name='about-us'),

    #sign-up
    # url(r'^signup/', core_views.signup, name='signup'),
    # url(r'^login/', auth_views.login, {'template_name': 'home/login.html'}, name='login'),
    # url(r'^logout/', auth_views.logout, {'next_page': '/'}, name='logout'),

    url(r'login/',login_view, name='login'),
    url(r'logout/',logout_view, name='logout'),
    url(r'register/',register_view, name='register'),
    ]