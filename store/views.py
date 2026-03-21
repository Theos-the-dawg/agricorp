from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import ExpenseEntry,Expense, Category, Product, Order
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, ExpenseEntryFormSet,LoginForm
from datetime import datetime
import pandas as pd
import plotly.express as px
import plotly.offline as py_offline
import matplotlib.pyplot as plt
from dateutil.relativedelta import relativedelta 
from django.utils import timezone
import mpld3
import numpy as np
from django.conf import settings


@csrf_exempt
def home_view(request):
    return render(request, 'home.html')

@login_required
def dashboard_view(request):
    """Dashboard view showing user's expenses and products"""
    user = request.user
    expenses = ExpenseEntry.objects.filter(reporter=user)
    total_expenses = sum(e.amount for e in expenses)
    recent_expenses = ExpenseEntry.objects.filter(reporter=user).values(
        'id', 'category', 'amount', 'expense__date'
    ).order_by('-expense__date')[:5]
    
    products = Product.objects.all()
    total_products = products.count()
    orders = Order.objects.all()
    total_orders = orders.count()
    
    context = {
        'total_expenses': total_expenses,
        'total_products': total_products,
        'total_orders': total_orders,
        'recent_expenses': recent_expenses,
        'products': products[:5],
    }
    return render(request, 'dashboard.html', context)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        registration_form = CustomUserCreationForm(request.POST)
        if registration_form.is_valid():
            user = registration_form.save()
            login(request, user)
            return redirect('home')
    else:
        registration_form = CustomUserCreationForm()
       
    return render(request, 'register.html', {'registration_form':  registration_form})

#session is controlled by django automatically
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
            if  authenticated_user is not None:
                login(request, authenticated_user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html', {'login_form': login_form})

#
def confirm_logout_view(request):
     if request.method =='POST' :
        logout(request)
        return redirect('home')

     else:
      context = {
        'username': request.user.username if request.user.is_authenticated else 'Guest',
        'message': 'Welcome to our website!',
             }
      return render(request, 'confirm_logout.html', context)


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



def plotly_chart_view(request):
    # Gather data from the DB and render both a bar and pie chart using Plotly
    user_expenses = ExpenseEntry.objects.values('reporter','expense__date','category','amount')
    user_expenses_df = pd.DataFrame(list(user_expenses))

    plot_div, plot_pie = make_plotly_divs(user_expenses_df)

    context = {'plot_div': plot_div, 'plot_pie': plot_pie}
    return render(request, 'chart.html', context)

def make_plotly_divs(df):
    """Return two Plotly HTML divs (bar and pie) for a given DataFrame.

    Both divs are returned with `include_plotlyjs=False` so the template
    can include the Plotly script once.
    """
    if df is None or df.empty:
        # Create minimal empty figures to avoid template errors
        bar_fig = px.bar(pd.DataFrame({'x':[], 'y':[]}), x='x', y='y', title='No data')
        pie_fig = px.pie(pd.DataFrame({'names':[], 'values':[]}), names='names', values='values', title='No data')
    else:
        # Ensure the columns exist
        # For the bar chart we show amounts over date grouped by category
        bar_fig = px.bar(df, x='expense__date', y='amount', color='category', title='Expenses over Time')
        # For the pie chart we aggregate by category
        agg = df.groupby('category', dropna=False)['amount'].sum().reset_index()
        pie_fig = px.pie(agg, values='amount', names='category', title='Expenses by Category')

    bar_div = py_offline.plot(bar_fig, auto_open=False, output_type='div', include_plotlyjs=False)
    pie_div = py_offline.plot(pie_fig, auto_open=False, output_type='div', include_plotlyjs=False)
    return bar_div, pie_div

# def make_pie_chart(request):
#     user_expenses = ExpenseEntry.objects.values('reporter','expense__date','category','amount')
#     user_expenses_df = pd.DataFrame(list(user_expenses))
#     plot_pie = make_plotly_divs(user_expenses_df)

#     context = {'plot_pie': plot_pie}
    return render(request,'chart.html', context)
    # df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
    # df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
    # fig = px.pie(df, values='pop', names='country', title='Population of European continent')
    # fig.show()

# List all categories
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def list_all_products(request):
    products = Product.objects.all()
    return render(request, 'products_list.html', {'products': products})

# List products in a category
def product_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'product_list.html', {'category': category, 'products': products})

# Product detail
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

# Place order
def place_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        Order.objects.create(product=product, quantity=quantity, ordered=True, order_date=timezone.now())
        return redirect('category_list')
    return render(request, 'place_order.html', {'product': product})

def cart_logic(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(ordered=False)
        return render(request, 'cart.html', {'orders': orders})
    else:
      return redirect('login')

def order_history(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(ordered=True).order_by('-order_date')
        return render(request, 'order_history.html', {'orders': orders})

