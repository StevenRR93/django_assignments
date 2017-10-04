# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from .models import Courses

from django.contrib import messages
from django.contrib.messages import error

def index(request):
    courses = Courses.objects.order_by('id').all()
    return render(request, 'courses.html', {'courses': courses})


def delete(request, idnum):
    course = Courses.objects.get(id = idnum)
    return render(request, 'courses/delete.html', {'course': course})

def create(request):
    if (request.method == "POST"):
        errors = Courses.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
        else:
            course = Courses.objects.create(name =request.POST['name'], description = request.POST['description'])
            course.save()
    return redirect('/courses')

def destroy(request, idnum):
    if (request.method == "POST"):
        Courses.objects.get(id = idnum).delete()
    return redirect('/courses')


