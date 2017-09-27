# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from models import *

def test(request):
   response = "Hello, I am your first request!"
   return HttpResponse(response)
# Create your views here.


