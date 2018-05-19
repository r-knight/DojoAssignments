from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'list', views.list, name='list'),
    url(r'(?P<review_id>\d+)/destroy', views.destroy, name='destroy'),
    url(r'(?P<book_id>\d+)', views.view_book, name='view'),
    url(r'add', views.add, name='add'),
    url(r'process_book', views.process_book, name='process_book'),
    url(r'review_existing', views.review_existing, name='review_existing'),
    url(r'^$', views.list, name ='list'),
]