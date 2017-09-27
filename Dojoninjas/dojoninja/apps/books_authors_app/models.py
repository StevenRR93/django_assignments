# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Books(models.Model):
    # id = models.PrimaryKey()
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Books object:{} {} {}>".format(self.id, self.name, self.desc)

class Authors(models.Model):
    # id = models.PrimaryKey()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    notes = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Authors object:{} {} {} {}>".format(self.author_id, self.first_name, self.last_name, self.email)

class Books_Authors(models.Model):
    book_id = models.ForeignKey(Books)
    author_id = models.ForeignKey(Authors)
    def __repr__(self):
        return "<Association object:{} {}>".format(self.book_id, self.author_id)
