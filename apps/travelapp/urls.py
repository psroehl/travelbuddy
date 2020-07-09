from django.conf.urls import url
from . import views     
               
urlpatterns = [
    url(r'^$', views.index),
    url(r'^dashboard$', views.dashboard),
    url(r'^create$', views.create),
    url(r'^add_trip$', views.add_trip),
    url(r'^details/(?P<num>\d+)$', views.details),
    url(r'^destroy/(?P<num>\d+)$', views.destroy),
    url(r'^edittrip/(?P<num>\d+)$', views.edittrip),
    url(r'^edittemp/(?P<num>\d+)$', views.edittemp),
    url(r'^reg$', views.reg),
    url(r'^logout', views.logout),
    url(r'^login', views.login),
]