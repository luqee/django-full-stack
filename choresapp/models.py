from django.db import models

# Create your models here.

class Client(models.Model):
    username = models.CharField(max_length=20, blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    token = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)

class Provider(models.Model):
    firstname = models.CharField(max_length=20, blank=True, null=True)
    lastname = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=20)
    token = models.CharField(max_length=200, blank=True, null=True)
    registered_as = models.CharField(max_length=20, blank=True, null=True)
    status = models.NullBooleanField()
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)

class Transaction(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    provider_id = models.ForeignKey(Provider, on_delete=models.CASCADE, blank=True, null=True)
    start_time = models.DateTimeField('start', blank=True, null=True)
    finish_time = models.DateTimeField('finish', blank=True, null=True)
    service_desc = models.TextField(blank=True, null=True)
    service_cost = models.FloatField(blank=True, null=True)

class Category(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
