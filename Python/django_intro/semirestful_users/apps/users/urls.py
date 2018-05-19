from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'new', views.new),
    url(r'(\d+)/edit', views.edit),
    url(r'(\d+)$', views.show),
    url(r'create', views.create),
    url(r'(\d+)/destroy', views.destroy),
    url(r'^update', views.update)
]