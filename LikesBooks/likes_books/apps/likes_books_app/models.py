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

class Books(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    uploaded_by_id = ForeignKey(Users)
    def __repr__(self):
        return "<Users object: {} {} {}>".format(self.id, self.name, self.desc)

class Likes(models.Model):
    user_id = ForeignKey(Users)
    book_id = ForeignKey(Books)
# Create your models here.
