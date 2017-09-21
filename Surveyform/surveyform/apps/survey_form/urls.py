from django.conf.urls import url
from views import *
urlpatterns = [ 
    url(r'^$', survey_form, name = 'survey'),
    url(r'^survey_form', survey_form, name='survey_form'),
    url(r'^results', results, name = 'results'),
    url(r'^process', process, name = 'process'),
]