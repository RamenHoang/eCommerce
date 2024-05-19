from django.db import models
from django.contrib.auth.models import User as Account


# Create your models here.

class Fullname(models.Model):
    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.firstname + " " + self.lastname

    class Meta:
        db_table = "full_names"


class Address(models.Model):
    no_house = models.CharField(max_length=200, null=True, default="")
    street = models.CharField(max_length=200, null=True, default="")
    city = models.CharField(max_length=200, null=True, default="")
    state = models.CharField(max_length=200, null=True, default="")
    zipcode = models.CharField(max_length=200, null=True, default="")

    def __str__(self):
        return self.no_house + "," + self.street + "," + self.city + "," + self.state + "," + self.zipcode

    class Meta:
        db_table = "addresses"
        verbose_name_plural = "Addresses"


class User(models.Model):
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, null=True, blank=True)
    fullname = models.ForeignKey(
        Fullname, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.ForeignKey(
        Address, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.fullname.__str__()

    class Meta:
        db_table = "users"
