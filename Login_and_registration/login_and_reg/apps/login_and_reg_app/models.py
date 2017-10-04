# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import re

class UsersManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        print(str(Users.objects.filter(email = postData['email'])))
        print(re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', postData['email']) != None)
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
        return errors

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Users object: {} {} {} {}>".format(self.id, self.first_name, self.last_name, self.email)
    # *************************
    # Connect an instance of UsersManager to our Users model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = UsersManager()
    # *************************

    
