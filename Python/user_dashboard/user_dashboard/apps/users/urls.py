from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^signin', views.signin ),
    url(r'^register', views.register),
    url(r'^logoff', views.new ),
    url(r'^users/new', views.new ),
    url(r'^users/show/(?P<id>\d+)', views.show),
    url(r'^users/edit/(?P<id>\d+)', views.edit_admin),
    url(r'^users/edit', views.edit ),
    url(r'^users/post_message', views.post_message ),
    url(r'^users/post_comment', views.post_comment ),
]