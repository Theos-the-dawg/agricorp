from django.db import models
from datetime import datetime

class Invoice(models.Model):
    Accounting =models.DecimalField(max_digits=10, decimal_places=2)
    Advertising =models.DecimalField(max_digits=10, decimal_places=2)
    Bank_charges = models.DecimalField(max_digits=10, decimal_places=2)
    Cleaning = models.DecimalField(max_digits=10, decimal_places=2)
    Borehole_Implements = models.DecimalField(max_digits=10, decimal_places=2)
    Tractor_hiring = models.DecimalField(max_digits=10, decimal_places=2)
    Tomato_Trellising_twine = models.DecimalField(max_digits=10, decimal_place)
    Consulting_Fees = models.DecimalField(max_digits=10, decimal_place)
    Council_Unit_Tax = models.DecimalField(max_digits=10, decimal_place)
    Medicines_Vet = models.DecimalField(max_digits=10, decimal_place)
    Fuels_Oils = models.DecimalField(max_digits=10, decimal_place)
    Spraying_chemicals = models.DecimalField(max_digits=10, decimal_place)
    General_expenses = models.DecimalField(max_digits=10, decimal_place)
    Insurance_licenses = models.DecimalField(max_digits=10, decimal_place)
    Stockfeeds = models.DecimalField(max_digits=10, decimal_place)
    M/V_Maintanance = models.DecimalField(max_digits=10, decimal_place)
    Tractor_Repairs = models.DecimalField(max_digits=10, decimal_place)
    Seeds_tomatoes = models.DecimalField(max_digits=10, decimal_place)
    seeds_beans = models.DecimalField(max_digits=10, decimal_place)
    Salaries_wages = models.DecimalField(max_digits=10, decimal_place)
    Security = models.DecimalField(max_digits=10, decimal_place)
    Fertiliser = models.DecimalField(max_digits=10, decimal_place)
    Telephones_Fax_Internet = models.DecimalField(max_digits=10, decimal_place)
    Training = models.DecimalField(max_digits=10, decimal_place)
    Travelling = models.DecimalField(max_digits=10, decimal_place)
    Staff_wefare = models.DecimalField(max_digits=10, decimal_place)
    Loan_Repayment = models.DecimalField(max_digits=10, decimal_place)

class Harvest(models.Model):
    crop = models.CharField(max_length=50)
    crops = models.JSONField()
    date_harvested= models.DateField(default=datetime.now())

def __str__(self):
    return self.crop