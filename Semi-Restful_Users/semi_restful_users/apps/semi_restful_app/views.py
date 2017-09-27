# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from .models import Users

import time

def index(request):
    users = Users.objects.order_by('id').all()
    return render(request, 'users.html', {'users': users})

def new(request):
    return render(request, 'users/new.html')

def edit(request, idnum):
    user = Users.objects.get(id = idnum)
    return render(request, 'users/edit.html', {'user': user})

def show(request, idnum):
    user = Users.objects.get(id = idnum)
    return render(request, 'users/show.html', {'user': user})

def create(request):
    if (request.method == "POST"):
        user = Users.objects.create(first_name =request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
        user.save()
        return redirect('/users/'+str(user.id))
    else:
        return redirect('/users')

def destroy(request, idnum):
    Users.objects.get(id = idnum).delete()
    return redirect('/users')

def update(request, idnum):
    if (request.method == "POST"):
        #errors = Users.objects.basic_validator(request.POST)
        #if len(errors):
        #    for tag, error in errors.iteritems():
        #        messages.error(request, error, extra_tags=tag)
        #    return redirect('/users'+str(idnum)+'/edit/')
        #else:
        user = Users.objects.get(id = idnum)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return redirect('/users/'+str(idnum))
    else:
        return redirect('/users')
# Create your views here.
