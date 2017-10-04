# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import datetime
import re

class UsersManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        #print(Users.objects.filter(email = postData['email']).exists())
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should have more than 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should have more than 2 characters"
        if len(postData['password']) < 8:
            errors['password'] = "Password should be more than 8 characters"
        if (not re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', postData['email'])):
            errors['email'] = "E-mail address should be a valid e-mail address"
        if (Users.objects.filter(email = postData['email']).exists()):
            errors['email'] = "E-mail address already used"
        if len(postData['alias']) < 2:
            errors["alias"] = "Alias should have more than 2 characters"
        if (Users.objects.filter(alias = postData['alias']).exists()):
            errors['alias'] = "Alias already used"
        return errors

class BookManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if (len(postData['author']) < 2) & (postData['authorsel'] == ""):
            errors["author"] = "Author should be more than 2 characters"
        if len(postData['title']) < 1:
            errors["title"] = "Title should exist"
        return errors

class ReviewManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['description']) < 5:
            errors["description"] = "Description should be more than 5 characters"
        if (int(postData['rating']) < 0) | (int(postData['rating']) > 5):
            errors["rating"] = "Rating should be between 0 and 5"
        return errors

class Users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    alias = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Users object: {} {} {} {} {}>".format(self.id, self.first_name, self.last_name, self.email, self. alias)
    # *************************
    # Connect an instance of UsersManager to our Users model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = UsersManager()
    # *************************

class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Books object: {} {} {}>".format(self.id, self.title, self.author) #, self.user
    # *************************
    # Connect an instance of UsersManager to our Users model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = BookManager()
    # *************************

class Reviews(models.Model):
    description = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Reviews object: {} {} {}>".format(self.id, self.description, self.rating ) #, self.user
    # *************************
    # Connect an instance of UsersManager to our Users model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = ReviewManager()
    # *************************

