from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^random_word$', views.index),
    url(r'^reset$', views.reset),
    url(r'^random_word/reset$', views.reset),
    url(r'^new$', views.new)
]
