from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+.[a-zA-Z]*$')

class UserManager(models.Manager):
    def register(self, first_name, last_name, email, password, confirm_password):
        errors = {}
        if len(first_name) < 2:
            errors['first_name'] = "First Name is too short."
        if len(last_name) < 2:
            errors['last_name'] = "Last Name is too short."
        if len(password) < 8:
            errors['password'] = "Password is too short."
        if password != confirm_password:
            errors['confirm_password'] = "Passwords do not match."
        if not EMAIL_REGEX.match(email):
            errors['email'] = "Not a valid email address."
        if errors:
            return (False, errors)
        else:
            password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            self.create(first_name=first_name, last_name=last_name, password=password, email=email)
            print 'Success!'

    def login(self, email, password):
        user = self.get(email=email)
        if user:
            print user.first_name
            print user.password

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    userManager = UserManager()
