from django.conf.urls import url
from views import *
urlpatterns = [ 
    url(r'^$', surveys, name = 'surveys'),
    url(r'^new', new, name = 'new'),
]