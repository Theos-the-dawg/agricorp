from django.db import models
from datetime import datetime

class Invoice(models.Model):
    Accounting =models.DecimalField(max_digits=10, decimal_places=2)
    Advertising =models.DecimalField(max_digits=10, decimal_places=2)
    Bank_Charges = models.DecimalField(max_digits=10, decimal_places=2)
    Cleaning = models.DecimalField(max_digits=10, decimal_places=2)
    Borehole_Implements = models.DecimalField(max_digits=10, decimal_places=2)
    Tractor_Hiring = models.DecimalField(max_digits=10, decimal_places=2)
    Tomato_Trellising_Twine = models.DecimalField(max_digits=10, decimal_places=2)
    Consulting_Fees = models.DecimalField(max_digits=10, decimal_places=2)
    Council_Unit_Tax = models.DecimalField(max_digits=10, decimal_places=2)
    Medicines_Vet = models.DecimalField(max_digits=10, decimal_places=2)
    Fuels_Oils = models.DecimalField(max_digits=10, decimal_places=2)
    Spraying_Chemicals = models.DecimalField(max_digits=10, decimal_places=2)
    General_Expenses = models.DecimalField(max_digits=10, decimal_places=2)
    Insurance_Licenses = models.DecimalField(max_digits=10, decimal_places=2)
    Stockfeeds = models.DecimalField(max_digits=10, decimal_places=2)
    MotorVehicle_Maintenance = models.DecimalField(max_digits=10, decimal_places=2)
    Tractor_Repairs = models.DecimalField(max_digits=10, decimal_places=2)
    Seeds_Tomatoes = models.DecimalField(max_digits=10, decimal_places=2)
    Seeds_Beans = models.DecimalField(max_digits=10, decimal_places=2)
    Salaries_Wages = models.DecimalField(max_digits=10, decimal_places=2)
    Security = models.DecimalField(max_digits=10, decimal_places=2)
    Fertiliser = models.DecimalField(max_digits=10, decimal_places=2)
    Telephones_Fax_Internet = models.DecimalField(max_digits=10, decimal_places=2)
    Training = models.DecimalField(max_digits=10, decimal_places=2)
    Travelling = models.DecimalField(max_digits=10, decimal_places=2)
    Staff_Welfare = models.DecimalField(max_digits=10, decimal_places=2)
    Loan_Repayment = models.DecimalField(max_digits=10, decimal_places=2)

class Harvest(models.Model):
    crop = models.CharField(max_length=50)
    crops = models.JSONField()
    date_harvested= models.DateField(default=datetime.now())

def __str__(self):
    return self.crop