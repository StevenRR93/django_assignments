# -*- coding: utf-8 -*-
#Steven Ramirez
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from .models import Users
from .models import Books
from .models import Reviews
from django.contrib import messages
from django.contrib.messages import error
import time
import bcrypt

def main(request):
    is_signed_in = request.session.get('is_signed_in', False)
    if (is_signed_in == True):
        return redirect('/books')
    return render(request, 'main.html')

def login(request):
    if (request.method == "POST"):
        try:
            user = Users.objects.get(email = request.POST['email'])
            if (bcrypt.checkpw(request.POST['password'].encode('utf8'), user.password.encode('utf8'))):
                request.session['first_name'] = user.first_name
                request.session['last_name'] = user.last_name
                request.session['alias'] = user.alias
                request.session['email'] = request.POST['email']
                request.session['id'] = user.id
                request.session['is_signed_in'] = True
                return redirect('/books')
            else: 
                messages.error(request, 'Incorrect password.')
                return redirect('/main')
        except:
            messages.error(request, 'E-mail address not found, please enter a valid e-mail.')
            return redirect('/main')
    else:
        return redirect('/main')
    
def register(request):
    if (request.method == "POST"):
        errors = Users.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/main')
        elif (request.POST['password'] == request.POST['confirmpw']):
            errors = Users.objects.basic_validator(request.POST)
            salt = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            user = Users.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = salt, alias = request.POST['alias'])
            user.save()
            return redirect('register/'+str(user.id))
        else:
            return redirect('/main')
    else:
        return redirect('/main')

def success_reg(request, idnum):
    user = Users.objects.get(id = idnum)
    return render(request, 'register.html', {'user': user})

def books(request):
    if request.session['is_signed_in'] == False:
        return redirect('/main')
        ## dd/mm/yyyy format
    try:
        user = Users.objects.get(id = request.session['id'])
        reviews = Reviews.objects.all().order_by('-created_at')[:3]
        your_reviews = Reviews.objects.filter(user = user.id).order_by('-created_at')
        if not reviews.exists():
            reviews = None
        if not your_reviews.exists():
            your_reviews = None
    except:
        reviews = None
        your_reviews = None
    try:
        alias = Reviews.objects.select_related('Users').all().alias
    except:
        alias = None
    try:
        books = Books.objects.all().order_by('title')
    except:
        books = None
    print(reviews)
    print(books)
    print(your_reviews)
    print(alias)
    return render(request, 'books.html', {'reviews' : reviews, 'books' : books, 'your_reviews': your_reviews , 'alias': alias} )

def show(request, idnum):
    if request.session['is_signed_in'] == False:
        return redirect('/main')
    try:
        book = Books.objects.get(id = idnum)
        reviews = Reviews.objects.select_related('book').filter(book_id = idnum).order_by('created_at')[:3]
    except:
        book = None
        reviews = None
    return render(request, 'books/show.html', {'book':book,'reviews':reviews})

def review(request):
    if request.session['is_signed_in'] == False:
        return redirect('/main')
    if (request.method == "POST"):
        review_errors = Reviews.objects.basic_validator(request.POST)
        if len(review_errors):
            for tag, error in review_errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('books/'+request.POST['idnum'])
        elif (request.session['is_signed_in'] == True):
            user = Users.objects.get(id = request.session['id'])
            book = Books.objects.get(id = request.POST['idnum'])
            book.save()
            review = Reviews.objects.create(rating = request.POST['rating'], description = request.POST['description'], user = user, book = book)
            review.save()
            return redirect('/books')
        else:
            return redirect('/books')
    else:
        return redirect('/main') 

def signout(request):
    if request.session['is_signed_in'] == False:
        return redirect('/main')
    request.session['first_name'] = None
    request.session['last_name'] = None
    request.session['email'] = None
    request.session['id'] = None
    request.session['is_signed_in'] = False
    return redirect('/main')

def add(request):
    if request.session['is_signed_in'] == False:
        return redirect('/main')
    try:
        books = Books.objects.all()
    except:
        books = None
        return redirect('/books')
    return render(request, 'books/add.html', {'books' : books })

def create(request):
    if request.session['is_signed_in'] == False:
        return redirect('/main')
    if (request.method == "POST"):
        if (request.POST['authorsel'] != ""):
            authorval = request.POST['authorsel']   
        else:
            authorval = request.POST['author']
        book_errors = Books.objects.basic_validator(request.POST)
        review_errors = Reviews.objects.basic_validator(request.POST)
        if len(book_errors):
            for tag, error in book_errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('books/add')
        elif len(review_errors):
            for tag, error in review_errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('books/add')
        elif (request.session['is_signed_in'] == True):
            user = Users.objects.get(id = request.session['id'])
            book = Books.objects.create(author = authorval, title = request.POST['title'])
            book.save()
            review = Reviews.objects.create(rating = request.POST['rating'], description = request.POST['description'], user = user, book = book)
            review.save()
            return redirect('/books')
        else:
            return redirect('/books')
    else:
        return redirect('/main')

def destroy(request, idnum):
    if request.session['is_signed_in'] == False:
        return redirect('/main')
    Books.objects.get(id = idnum).delete()
    return redirect('/books')

def users(request, idnum):
    if request.session['is_signed_in'] == False:
        return redirect('/main')
    try:
        user = Users.objects.get(id = idnum)
        reviews = Reviews.objects.filter(user_id = idnum)
        rcount = Reviews.objects.filter(user_id = idnum).count()
        return render(request, "users/users.html", {'user' : user, 'reviews' : reviews, 'rcount': rcount})
    except:
        return redirect('/books')
    return redirect('/books')

def fullstar(request):
    image_data = open("/fullstar.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")

def emptystar(request):
    image_data = open("emptystar.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")

# Create your views here.
