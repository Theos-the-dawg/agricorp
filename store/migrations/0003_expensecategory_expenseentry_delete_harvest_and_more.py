# Generated by Django 4.1 on 2024-09-24 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_invoice_alter_harvest_date_harvested'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Accounting', 'Accounting'), ('Advertising', 'Advertising'), ('Bank Charges', 'Bank Charges'), ('Cleaning', 'Cleaning'), ('Borehole Implements', 'Borehole Implements'), ('Tractor Hiring', 'Tractor Hiring'), ('Tomato Trellising Twine', 'Tomato Trellising Twine'), ('Consulting Fees', 'Consulting Fees'), ('Council Unit Tax', 'Council Unit Tax'), ('Medicines Vet', 'Medicines Vet'), ('Fuels Oils', 'Fuels Oils'), ('Spraying Chemicals', 'Spraying Chemicals'), ('General Expenses', 'General Expenses'), ('Insurance Licenses', 'Insurance Licenses'), ('Stockfeeds', 'Stockfeeds'), ('MotorVehicle Maintenance', 'MotorVehicle Maintenance'), ('Tractor Repairs', 'Tractor Repairs'), ('Seeds Tomatoes', 'Seeds Tomatoes'), ('Seeds Beans', 'Seeds Beans'), ('Salaries Wages', 'Salaries Wages'), ('Security', 'Security'), ('Fertiliser', 'Fertiliser'), ('Telephones Fax Internet', 'Telephones Fax Internet'), ('Training', 'Training'), ('Travelling', 'Travelling'), ('Staff Welfare', 'Staff Welfare'), ('Loan Repayment', 'Loan Repayment')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.expensecategory')),
            ],
        ),
        migrations.DeleteModel(
            name='Harvest',
        ),
        migrations.DeleteModel(
            name='Invoice',
        ),
    ]