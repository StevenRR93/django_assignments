# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

import time

def session_words(request):
    return render(request, 'session_words.html')

def clear(request):
    request.session['wordlist'] = []
    return redirect('/session_words')

def word(request):
    if (request.method == "POST"):
        word = request.session.get('wordlist', [])
        request.session['wordlist'] = word
        print(word)
        dictionary = {}
        dictionary['time'] = time.strftime("%I:%M:%S%p, %B %d %Y")
        dictionary['string'] = request.POST.get('string', "")
        dictionary['color'] = request.POST.get('color', "red")
        if (request.POST.get('font', False)):
            dictionary['font'] = "30px"
        else :
            dictionary['font'] = "18px"
        request.session['wordlist'].append(dictionary)
        return redirect('/session_words')
    else:
	    return redirect('/session_words')

# Create your views here.
