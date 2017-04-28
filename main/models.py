from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


# Create your models here.

class Building(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    owner = models.ForeignKey(User, related_name='building')
    concierges = models.ManyToManyField(User)

    def __unicode__(self):
        return str(self.id)


class Apartment(models.Model):
    number = models.IntegerField(unique=True)
    floor = models.IntegerField()
    building = models.ForeignKey(Building, related_name='apartment')
    residents = models.ManyToManyField(User)

    def __unicode__(self):
        return str(self.id)


class Visit(models.Model):
    name = models.CharField(max_length=60)
    rut = models.CharField(max_length=12)
    date = models.DateTimeField(default=datetime.now)
    apartment = models.ForeignKey(Apartment)
    resident = models.ForeignKey(User)
    note = models.TextField(max_length=200)
    received = models.BooleanField(default=True)
    consierge = models.ForeignKey(User)

    def __unicode__(self):
        return str(self.id)


class Publication(models.Model):
    publisher = models.ForeignKey(User, related_name='publication')
    title = models.CharField(max_length=100)
    date = models.DateField(default=datetime.now)
    hour = models.TimeField(default=datetime.now)
    message = models.TextField(max_length=1000)
    type = models.CharField(max_length=100)

    def __unicode__(self):
        return str(self.id)


class Location(models.Model):
    name = models.CharField(max_length=100)
    building = models.ForeignKey(Building, related_name='location')

    def __unicode__(self):
        return str(self.id)


class Event(models.Model):
    title = models.CharField(max_length=100)
    start = models.CharField(max_length=100)
    end = models.CharField(max_length=100)
    all_day = models.IntegerField()
    resident = models.ForeignKey(User, related_name='event')
    location = models.ForeignKey(Location, related_name='event')

    def __unicode__(self):
        return str(self.id)


class Rent(models.Model):
    month = models.CharField(max_length=50)
    amount = models.IntegerField()
    resident = models.ForeignKey(User, related_name='rent')
    date = models.DateTimeField(default=datetime.now())

    def __unicode__(self):
        return str(self.id)