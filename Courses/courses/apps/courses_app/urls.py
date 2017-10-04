from django.conf.urls import url
from views import *
urlpatterns = [ 
   url(r'^$', index, name = 'index'), 
   url(r'^courses$', index, name = 'index'),
   url(r'^courses/create$', create, name = 'create'),
   url(r'^courses/destroy/([1-9]+)$', destroy, name = 'destroy'),
   url(r'^courses/delete/([1-9]+)$', delete, name = 'delete'),
]