from django.conf.urls import url
from .import views

app_name='home'
urlpatterns = [
    #/home/
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'innovation/$' , views.InnovationView.as_view(), name='innovation' ),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #home/innovation/addInnovation
    url(r'innovation/add/$', views.InnovationCreate.as_view(), name='inn-add'),
    url(r'(?P<pk>[0-9]+)/edit/$', views.InnovationUpdate.as_view(), name='inn-update'),

    ]