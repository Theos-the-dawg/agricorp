from django.db import models
from datetime import datetime

class Invoice(models.Model):
    Accounting =models.DecimalField(max_digits=10, decimal_places=2)
    Advertising =models.DecimalField(max_digits=10, decimal_places=2)
    Bank_charges = models.DecimalField(max_digits=10, decimal_places=2)
    Cleaning = models.DecimalField(max_digits=10, decimal_places=2)
    Borehole_Implements = models.DecimalField(max_digits=10, decimal_places=2)
    Tractor_hiring = models.DecimalField(max_digits=10, decimal_places=2)
    Tomato_Trellising_twine = models.DecimalField(max_digits=10, decimal_place=2)
    Consulting_Fees = models.DecimalField(max_digits=10, decimal_place=2)
    Council_Unit_Tax = models.DecimalField(max_digits=10, decimal_place=2)
    Medicines_Vet = models.DecimalField(max_digits=10, decimal_place=2)
    Fuels_Oils = models.DecimalField(max_digits=10, decimal_place=2)
    Spraying_chemicals = models.DecimalField(max_digits=10, decimal_place=2)
    General_expenses = models.DecimalField(max_digits=10, decimal_place=2)
    Insurance_licenses = models.DecimalField(max_digits=10, decimal_place=2)
    Stockfeeds = models.DecimalField(max_digits=10, decimal_place=2)
    M/V_Maintanance = models.DecimalField(max_digits=10, decimal_place=2)
    Tractor_Repairs = models.DecimalField(max_digits=10, decimal_place=2)
    Seeds_tomatoes = models.DecimalField(max_digits=10, decimal_place=2)
    seeds_beans = models.DecimalField(max_digits=10, decimal_place=2)
    Salaries_wages = models.DecimalField(max_digits=10, decimal_place=2)
    Security = models.DecimalField(max_digits=10, decimal_place=2)
    Fertiliser = models.DecimalField(max_digits=10, decimal_place=2)
    Telephones_Fax_Internet = models.DecimalField(max_digits=10, decimal_place=2)
    Training = models.DecimalField(max_digits=10, decimal_place=2)
    Travelling = models.DecimalField(max_digits=10, decimal_place=2)
    Staff_wefare = models.DecimalField(max_digits=10, decimal_place=2)
    Loan_Repayment = models.DecimalField(max_digits=10, decimal_place=2)

class Harvest(models.Model):
    crop = models.CharField(max_length=50)
    crops = models.JSONField()
    date_harvested= models.DateField(default=datetime.now())

def __str__(self):
    return self.crop