from django.conf.urls import url
from views import *
urlpatterns = [ 
   url(r'^$', index, name = 'users'),
   url(r'^users$', index, name = 'users'), 
   url(r'^users/new$', new, name = 'new'), 
   url(r'^users/([0-9]+)/edit$', edit, name = 'edit'),
   url(r'^users/([0-9]+)$', show, name = 'show'),
   url(r'^users/create$', create, name = 'create'),
   url(r'^users/([0-9]+)/destroy$', destroy, name = 'destroy'),
   url(r'^users/([0-9]+)/update$', update, name = 'update'),
]