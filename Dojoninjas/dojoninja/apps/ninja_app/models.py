# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Dojos(models.Model):
    # id = models.PrimaryKey()
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.CharField(max_length=255)
    def __repr__(self):
        return "<Dojos object:{} {} {} {}>".format(self.id, self.name, self.city, self.state)

class Ninjas(models.Model):
    # id = models.PrimaryKey()
    dojos_id = models.ForeignKey(Dojos)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    def __repr__(self):
        return "<Ninjas object:{} {} {}>".format(self.dojo_id, self.first_name, self.last_name)


