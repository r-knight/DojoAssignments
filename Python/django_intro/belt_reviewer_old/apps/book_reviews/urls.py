from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'list', views.list),
    url(r'(\d+)/destroy', views.destroy),
    url(r'(\d+)', views.view_book),
    url(r'add', views.add),
    url(r'process_book', views.process_book),
    url(r'review_existing', views.review_existing),
    url(r'^$', views.list),
]