# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def register(request):
    response = "Placeholder to display all the surveys created"
    return HttpResponse(response)   
    #return render(request, 'users/index.html')

def login(request):
    response = "Placeholder for users to login"
    return HttpResponse(response)

def new(request):
    response = "Placeholder to later display all the list of users"
    return HttpResponse(response)

def users(request):
    response = "Placeholder to display all the surveys created"
    return HttpResponse(response)

# Create your views here.
