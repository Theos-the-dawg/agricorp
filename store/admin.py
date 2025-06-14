from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(ExpenseEntry)
admin.site.register(ExpenseCategory)
admin.site.register(Expense)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)