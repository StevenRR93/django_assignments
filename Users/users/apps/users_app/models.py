# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
  # Create your models here.
def validate_age(value):
    if value < 0 | value > 150:
        raise ValidationError('%s is not a human age' % value)

def validate_name(name):
    if name.length < 1 | name.lenth > 25:
        raise ValidationError('%s is not a valid name' % name)

def validateEmail( email ):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email( email )
        return True
    except ValidationError:
        return False

class Users(models.Model):
    id = models.= models.PrimaryKey(User, unique=True)
    first_name = models.CharField(max_length=255, validators=[validate_name])
    last_name = models.CharField(max_length=255, validators=[validate_name])
    email_address = models.CharField(max_length=255, validators=[validateEmail], unique=True)
    age = models.IntegerField(validators=[validate_age])
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
