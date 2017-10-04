from django.conf.urls import url
from views import *
urlpatterns = [ 
   url(r'^$', main, name = 'main'), 
    url(r'^main$', main, name = 'main'),
    url(r'^login$', login, name = 'login'),
    url(r'^register$', register, name = 'register'),
    url(r'^books$', books, name = 'books'),
    url(r'^register/([0-9]+)', success_reg, name = 'success_reg'),
    url(r'^books/add$', add, name = 'add'),
    url(r'^create$', create, name = 'create'),
    url(r'^signout$', signout, name = 'signout'),
    url(r'^books/([0-9]+)', show, name = 'show'),
    url(r'^destroy/([0-9]+)', destroy, name = 'destroy'),
    url(r'^users/([0-9]+)', users, name = 'users'),
    url(r'^review$', review, name = 'review'),
    url(r'^fullstar$', fullstar, name = 'fullstar'),
    url(r'^emptystar$', emptystar, name = 'emptystar')
]