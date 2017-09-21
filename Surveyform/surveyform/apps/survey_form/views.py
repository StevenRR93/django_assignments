# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def survey_form(request):
    return render(request, 'survey_form.html')

def results(request):
    
    return render(request, 'results.html')

def process(request):
    if (request.method == "POST"):
        count = request.session.get('count', 0)
        request.session['count'] = count
        request.session['count'] += 1
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['message']
        return redirect('/results')
    else:
	    return redirect('/results')

# Create your views here.
