from django.conf.urls import url
from views import *
urlpatterns = [ 
    url(r'^$', amadon, name = 'amadon'),
    url(r'^amadon', amadon, name='amadom'),
    url(r'^amadon/checkout', checkout, name = 'checkout'),
    url(r'^amadon/buy', buy, name = 'buy'),
]