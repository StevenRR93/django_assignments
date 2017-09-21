# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    count = request.session.get('counter', 0)
    request.session['counter'] = count
    request.session['counter'] += 1
    request.session['value'] = get_random_string(length=14)
    return render(request, 'random_word.html')

def reset(request):
    request.session['counter'] = 0
    request.session['value'] = get_random_string(length=14)
    return redirect('/random_word')

# Create your views here.
