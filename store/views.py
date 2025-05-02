from django.contrib.auth.forms import UsernameField
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import ExpenseEntry,Expense
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, ExpenseEntryFormSet,LoginForm
from datetime import datetime
from  pandas import pandas as pd
from dateutil.relativedelta import relativedelta
import pdb


@csrf_exempt
def home_view(request):
    return render(request, 'home.html')

@csrf_exempt
def register(request):
    if request.method == 'POST':
        registration_form = CustomUserCreationForm(request.POST)
       
        if  registration_form.is_valid():
            user =  registration_form.save()
           
            login(request, user)  
           
            return redirect('home') 
    else:
        registration_form = CustomUserCreationForm()
       
    return render(request, 'register.html', {'registration_form':  registration_form})

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
    else:
        login_form = LoginForm(None)
    
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
            messages.error(request, "Username or password is incorrect.")

        if user is not None:
            # Authenticate the user
            authenticated_user = authenticate(request, username=username, password=password)
            if authenticated_user.is_authenticated:
                login(request, authenticated_user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html', {'login_form': login_form})


def confirm_logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
    else:
       return redirect('login')    


@login_required
def add_expenses(request):
    if request.method == 'POST':
        formset = ExpenseEntryFormSet(request.POST)
        if formset.is_valid():
            expense = Expense.objects.create(date=datetime.now())
            reporter_id = request.user.id
            for form in formset:
                if form.cleaned_data:
                    ExpenseEntry.objects.create(
                        reporter_id=reporter_id,
                        expense=expense,
                        category=form.cleaned_data['category'],
                        amount=form.cleaned_data['amount']
                    )
            return redirect('home') 
    else:
        formset = ExpenseEntryFormSet()

    return render(request, 'add_expenses.html', {'formset': formset})
    
@login_required
def generate_dataframe(request):

    #average for daily 
    todays_expense = (ExpenseEntry.objects
                      .filter(expense__date=datetime.today())
                      .values('id','expense','expense_id','category','amount','expense__date'))
    todays_expense_df = pd.DataFrame(list(todays_expense))
    print(todays_expense_df)#dataframe contain data for the day 


    #average for weekly
    today = datetime.today()
    last_week_date =today - relativedelta(weeks=1)
    weeks_expense = (ExpenseEntry.objects
                     .filter(expense__date__range=[last_week_date,today])
                     .values('id','expense','expense_id','category','amount','expense__date'))
    weekly_df = pd.DataFrame(list(weeks_expense))
    print(weekly_df)

    #average for monlthy
    today = datetime.today()
    last_month_date =today - relativedelta(months=1)
    month_expense = (ExpenseEntry.objects
                     .filter(expense__date__range=[last_month_date,today])
                     .values('id','expense','expense_id','category','amount','expense__date'))
    monthly_df = pd.DataFrame(list(month_expense))
    print(monthly_df)

  
    #average for yearly  today = datetime.today()
    last_years_date = datetime.today() - relativedelta(years=1)
    year_expense = (ExpenseEntry.objects
                    .filter(expense__date__range=[last_years_date,today])
                    .values('id','expense','expense_id','category','amount','expense__date'))
    yearly_df = pd.DataFrame(list(year_expense))
    print(yearly_df)
    


    # Convert DataFrame to HTML
    daily_df = todays_expense_df.to_html(classes="table table-striped", index=False)  # Use Bootstrap table classes for styling
    weekly_df_html = weekly_df.to_html(classes="table table-striped", index=False)
    monthly_df_html = monthly_df.to_html(classes="table table-striped", index=False)
    yearly_df_html = yearly_df.to_html(classes="table table-striped", index=False)

    # Pass the HTML table to the template
    return render(request, 'dataframe.html', {'daily_df': daily_df,#change name to fit with other fir df names
                                              'weekly_df':weekly_df_html,
                                              'monthly_df':monthly_df_html,
                                              'yearly_df':yearly_df_html})
    