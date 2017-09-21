# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

#def index(request):
#   response = "Hello, I am your first request!"
#   return redirect('some-view-name', foo='bar')
#   return HttpResponse(response)

#def yourMethodFromUrls(request):
#  context = {
#  "somekey":"somevalue"
#  }
#  return render(request,'page.html', context)

def index(request):
    context = {
    "time": strftime("%b %d, %y %I:%M %p", gmtime())
    }
    return render(request,'page.html', context)
# Create your views here.
