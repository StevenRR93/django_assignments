# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def index(request):
    response = "Placeholder to later display all the list of blogs"
    return HttpResponse(response)   
    #return render(request, 'users/index.html')

def new(request):
    response = "Placeholder to display a new form to create a new blog"
    return HttpResponse(response)
    
def create(request):
    return render(request, 'blogs.html')

def show(request, number):
    response = "Placeholder to display blog "+str(number)
    return HttpResponse(response)

def edit(request):
    response = "Placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def destroy(request):
    response = "Placeholder to display a new form to create a new blog"
    return HttpResponse(response)
#    /blogs/create - Have this be handled by a method named 'create'.  For now, have this url redirect to /blogs.
#/blogs/{{number}} - display 'placeholder to display blog {{number}}.  For example /blogs/15 should display a message 'placeholder to display blog 15'.  Have this be handled by a method named 'show'.
#/blogs/{{number}}/edit - display 'placeholder to edit blog {{number}}.  Have this be handled by a method named 'edit'.
#/blogs/{{number}}/delete - Have this be handled by a method named 'destroy'. For now, have this url redirect to /blogs. 

# Create your views here.
