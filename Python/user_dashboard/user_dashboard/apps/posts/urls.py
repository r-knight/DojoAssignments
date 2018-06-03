from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^signin', views.signin ),
    url(r'^register', views.register),
    url(r'^dashboard/admin', views.dashboard_admin ),
    url(r'^dashboard', views.dashboard),
    url(r'^users/new', views.new ),
    url(r'^users/show/?P<user_id>\d+', views.show),
    url(r'^users/edit/?P<user_id>\d+', views.edit_admin),
    url(r'^users/edit', views.signin ),
]