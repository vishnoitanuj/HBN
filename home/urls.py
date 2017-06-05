from django.conf.urls import url
from .import views
from django.views.generic.dates import ArchiveIndexView
from home.models import Innovation

app_name='home'
urlpatterns = [
    #/home/
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'innovation/$' , views.innovation_list, name='innovation' ),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #home/innovation/addInnovation
    url(r'innovation/add/$', views.InnovationCreate.as_view(), name='inn-add'),
        url(r'(?P<pk>[0-9]+)/edit/$', views.InnovationUpdate.as_view(), name='inn-update'),
    url(r'(?P<pk>[0-9]+)/delete/$', views.InnovationDelete.as_view(), name='inn-delete'),

    ]