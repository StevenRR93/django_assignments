# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from django import forms

def amadon(request):
    return render(request, 'amadon.html')

def checkout(request):
    print("session")
    print(request.session['total_purchased'])
    print(request.session['total_items'])
    print(request.session['last_purchase'])
    return render(request, 'amadon/checkout.html')

def buy(request):
    if (request.method == "POST"):
        total_items = request.session.get('total_items', 0)
        request.session['total_items'] = total_items
        total_purchased = request.session.get('total_purchased', 0)
        request.session['total_purchased'] = total_purchased
        product_id = request.POST['product_id']
        if (product_id == "1000"):
            request.session['total_items'] += int(request.POST['tshirt'])
            request.session['total_purchased'] += float(request.POST['tshirt'])* 19.99
            request.session['last_purchase'] = float(request.POST['tshirt'])* 19.99
        elif (product_id == "1001"):
            request.session['total_items'] += int(request.POST['sweater'])
            request.session['total_purchased'] += float(request.POST['sweater'])* 29.99
            request.session['last_purchase'] = float(request.POST['sweater'])* 29.99
        elif (product_id == "1002"):
            request.session['total_items'] += int(request.POST['cup'])
            request.session['total_purchased'] += float(request.POST['cup'])* 4.99
            request.session['last_purchase'] = float(request.POST['cup'])* 4.99
        elif (product_id == "1003"):
            request.session['total_items'] += int(request.POST['book'])
            request.session['total_purchased'] += float(request.POST['book'])* 49.99
            request.session['last_purchase'] = float(request.POST['book'])* 49.99
        else:
            request.session['last_purchase'] = 0.00
    return redirect("amadon/checkout")
    
