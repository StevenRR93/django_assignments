from django.conf.urls import url, include
from views import *
urlpatterns = [ 
    url(r'^$', amadon, name = 'amadon'),
    url(r'^amadon$', amadon, name='amadon'),
    url(r'^amadon/checkout$', checkout, name = 'checkout'),
    url(r'^buy$', buy, name = 'buy'),
]