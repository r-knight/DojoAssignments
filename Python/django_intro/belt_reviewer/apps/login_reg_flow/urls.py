from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'login', views.login, name ='login'),
	url(r'logout', views.logout, name ='logout'),
	url(r'register', views.register, name ='register'),
	url(r'success', views.success, name ='success'),
    url(r'(?P<user_id>\d+)', views.view_user, name ='view'),
	url(r'index', views.index, name ='index'),
	url(r'^$', views.index, name ='index'),
]
