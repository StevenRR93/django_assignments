# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Users object: {} {} {} {}>".format(self.id, self.first_name, self.last_name, self.email)
    # *************************
    # Connect an instance of BlogManager to our Blog model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    # objects = UsersManager()
    # *************************

# class UsersManager(models.Manager):
    # def basic_validator(self, postData):
        # errors = {}
        # if len(postData['first_name']) < 1:
            # errors["first_name"] = "First name should not be blank"
        # if len(postData['last_name']) < 1:
            # errors["last_name"] = "Blog desc should not be blank"
        # return errors
    