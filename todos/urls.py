from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<id>[0-9]+)/$', views.details),
    url(r'^add/$', views.add, name='add')
]
