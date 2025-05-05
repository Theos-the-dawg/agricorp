from django.contrib import admin
from .models import ExpenseCategory,ExpenseEntry,Expense
# Register your models here.
admin.site.register(ExpenseEntry)
admin.site.register(ExpenseCategory)
admin.site.register(Expense)