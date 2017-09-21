# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def amadon(request):
    return render(request, 'amadon.html')

def checkout(request):
    request.session['wordlist'] = []
    return render(request, 'checkout.html')

def buy(request):
    if (request.method == "POST"):
        word = request.session.get('wordlist', [])
        request.session['wordlist'] = word
        dictionary = {}
        dictionary['time'] = time.strftime("%I:%M:%S%p, %B %d %Y")
        dictionary['string'] = request.POST.get('string', "")
        dictionary['color'] = request.POST.get('color', "red")
        if (request.POST.get('font', False)):
            dictionary['font'] = "30px"
        else :
            dictionary['font'] = "18px"
        request.session['wordlist'].append(dictionary)
        return redirect('/checkout')
    else:
	    return redirect('/checkout')
