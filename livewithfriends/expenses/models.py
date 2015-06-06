from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    number = models.IntegerField()
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)

class Store(models.Model):

    # Name
    name = models.CharField(max_length=200)

    # Address
    address = models.ForeignKey(Address)

    # Phone number
    phone_number = models.IntegerField()

    # Notes  
    notes = models.CharField(max_length=400)

class House(models.Model):
    
    # Users who live in the house
    members = models.ManyToManyField(User, null=True)
    
    # Name
    name = models.CharField(max_length=200)
    
    # Address
    address = models.ForeignKey(Address, null=True)

    # Notes
    notes = models.CharField(max_length=200, null=True)

class Expense(models.Model):
    
    # Date of expense
    purchase_date = models.DateTimeField('date purchase')

    # Amount 
    amount = models.DecimalField(max_digits=7, decimal_places=2)

    # Payment method
    CASH = 'Ca'
    CREDIT = 'Cr'
    DEBIT = 'De'
    CHECK = 'Ch'
    PAYMENT_CHOICES = (
        (CASH, 'Cash'),
        (CREDIT, 'Credit'),
        (DEBIT, 'Debit'),
        (CHECK, 'Check')
    )
    payment_method = models.CharField(max_length=2, choices=PAYMENT_CHOICES, default=DEBIT)

    # Notes
    notes = models.CharField(max_length=400)

    #Creator
    creator = models.ForeignKey(User)

    # Store
    store = models.ForeignKey(Store)

    # House
    house = models.ForeignKey(House)

