from __future__ import unicode_literals
from django.db import models
import re

class travelManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['Destination']) < 5:
            errors['Destination'] = "Destination should be at least 5 letters long"
        if len(postData['Plan']) < 5:
            errors["Plan"] = "Plan should be at least 5 characters"
        return errors

class userManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['Email']):    # test whether a field matches the pattern            
            errors['Email'] = ("Invalid email address!")
        if len(postData['Fname']) < 2:
            errors['Fname'] = "First Name should be at least 2 letters long"
        if len(postData['Lname']) < 2:
            errors["Lname"] = "Last Name should be at least 2 characters"
        if len(postData['Password']) < 2:
            errors['Password'] = "Password should be at least 2 characters"
        if postData["Password"] != postData['Confirm']:
            errors ['err'] = "no match"
        
        return errors
    def sec_validator(self, postData):   
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['Email']):    # test whether a field matches the pattern            
            errors['Email'] = ("Invalid email address!")
        if len(postData['Password']) < 2:
            errors['Password'] = "Password should be at least 2 characters"
        return errors


class user(models.Model):
    Fname = models.CharField(max_length=45)
    Lname = models.CharField(max_length=45)
    Email = models.CharField(max_length=45)
    Password = models.CharField(max_length=45)
    objects = userManager()

class travel(models.Model):
    Destination = models.CharField(max_length=45)
    Plan = models.CharField(max_length=45)
    Start_date = models.DateTimeField()
    End_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(user, related_name="travels")
    objects = travelManager()
