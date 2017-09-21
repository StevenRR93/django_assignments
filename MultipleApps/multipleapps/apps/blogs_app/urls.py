from django.conf.urls import url
from views import *
urlpatterns = [ 
    url(r'^$', index, name = 'blogs'),
    url(r'^new', new, name = 'new'),
    url(r'^create', create, name = 'create'),
    url(r'^(?P<number>[0-9]+)/$', show, name = "number"),
    url(r'^edit', new, name = 'edit'),
    url(r'^destroy', create, name = 'destroy'),
]
