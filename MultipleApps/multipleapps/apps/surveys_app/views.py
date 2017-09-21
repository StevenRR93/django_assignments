# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def surveys(request):
    response = "Placeholder to display all the surveys created"
    return HttpResponse(response)   
    #return render(request, 'users/index.html')

def new(request):
    response = "Placeholder for users to add a new survey"
    return HttpResponse(response)
    
# Create your views here.
