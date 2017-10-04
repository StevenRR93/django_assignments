# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from .models import Users
from django.contrib import messages
from django.contrib.messages import error

import bcrypt

def home(request):
    is_signed_in = request.session.get('is_signed_in', False)
    if (is_signed_in == True):
        return redirect('/success/login')
    return render(request, 'home.html')

def login(request):
    if (request.method == "POST"):
        try:
            user = Users.objects.get(email = request.POST['email'])
            if (bcrypt.checkpw(request.POST['password'].encode('utf8'), user.password.encode('utf8'))):
                request.session['first_name'] = user.first_name
                request.session['last_name'] = user.last_name
                request.session['email'] = request.POST['email']
                request.session['is_signed_in'] = True
                return redirect('/success/login')
            else: 
                messages.error(request, 'Incorrect password.')
                return redirect('/home')
        except:
            messages.error(request, 'E-mail address not found, please enter a valid e-mail.')
            return redirect('/home')
    else:
        return redirect('/home')
    

def register(request):
    if (request.method == "POST"):
        errors = Users.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/home')
        elif (request.POST['password'] == request.POST['confirmpw']):
            errors = Users.objects.basic_validator(request.POST)
            salt = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            user = Users.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = salt)
            user.save()
            return redirect('success/register/'+str(user.id))
        else:
            return redirect('/home')
    else:
        return redirect('/home')

def success_reg(request, idnum):
    user = Users.objects.get(id = idnum)
    return render(request, 'success/register.html', {'user': user})

def success_log(request):
    if request.session['is_signed_in'] == False:
        return redirect('/home')
    return render(request, 'success/login.html')

def signout(request):
    request.session['first_name'] = None
    request.session['last_name'] = None
    request.session['email'] = None
    request.session['is_signed_in'] = False
    return redirect('/home')
# Create your views here.
