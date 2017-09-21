from django.conf.urls import url
from views import *
urlpatterns = [ 
    url(r'^$', session_words, name = 'session_words'),
    url(r'^session_words', session_words, name='session_words'),
    url(r'^add_word', word, name = 'word'),
    url(r'^clear', clear, name = 'clear'),
]