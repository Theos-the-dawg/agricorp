from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):
    date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Expenses for {self.date}"


class ExpenseCategory(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name="entries")
    category_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.category_name}: {self.amount}"
    

CATEGORY_CHOICES = [
     ('Accounting', 'Accounting'),
        ('Advertising', 'Advertising'),
        ('Bank Charges', 'Bank Charges'),
        ('Cleaning', 'Cleaning'),
        ('Borehole Implements', 'Borehole Implements'),
        ('Tractor Hiring', 'Tractor Hiring'),
        ('Tomato Trellising Twine', 'Tomato Trellising Twine'),
        ('Consulting Fees', 'Consulting Fees'),
        ('Council Unit Tax', 'Council Unit Tax'),
        ('Medicines Vet', 'Medicines Vet'),
        ('Fuels Oils', 'Fuels Oils'),
        ('Spraying Chemicals', 'Spraying Chemicals'),
        ('General Expenses', 'General Expenses'),
        ('Insurance Licenses', 'Insurance Licenses'),
        ('Stockfeeds', 'Stockfeeds'),
        ('MotorVehicle Maintenance', 'MotorVehicle Maintenance'),
        ('Tractor Repairs', 'Tractor Repairs'),
        ('Seeds Tomatoes', 'Seeds Tomatoes'),
        ('Seeds Beans', 'Seeds Beans'),
        ('Salaries Wages', 'Salaries Wages'),
        ('Security', 'Security'),
        ('Fertiliser', 'Fertiliser'),
        ('Telephones Fax Internet', 'Telephones Fax Internet'),
        ('Training', 'Training'),
        ('Travelling', 'Travelling'),
        ('Staff Welfare', 'Staff Welfare'),
        ('Loan Repayment', 'Loan Repayment'),
]

class ExpenseEntry(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='reporter')
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name='expense_entries')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.category} - {self.amount}"
