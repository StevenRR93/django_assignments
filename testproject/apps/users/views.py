# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def index(request):
        #response = "Hello, I am your first request!"
        return render(request, 'users/index.html')

# Create your views here.
