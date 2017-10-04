from django.conf.urls import url
from views import *
urlpatterns = [ 
    url(r'^$', home, name = 'home'), 
    url(r'^home$', home, name = 'home'),
    url(r'^login$', login, name = 'login'),
    url(r'^register$', register, name = 'register'),
    url(r'^success/login', success_log, name = 'success_log'),
    url(r'^success/register/([0-9]+)', success_reg, name = 'success_reg'),
    url(r'^signout', signout, name = 'signout')
]
