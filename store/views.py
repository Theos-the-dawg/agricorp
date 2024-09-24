from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import ExpenseEntry,Expense
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, ExpenseEntryFormSet,LoginForm
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

@csrf_exempt
def home_view(request):

    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            try:
                user = User.objects.get(email=email)
            except user.DoesNotExist:
                user = None
                messages.error(request, 'User does not exist.')

            if user is not None:
                # Authenticate the user
                authenticated_user = authenticate(request, email=email, password=password)
                if authenticated_user is not None:
                    login(request, authenticated_user)
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid email or password.')              

    return render(request, 'login.html', {'form': form})



def confirm_logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    else:
       return redirect('login')    

def add_expenses(request):
    if request.method == 'POST':
        formset = ExpenseEntryFormSet(request.POST)
        if formset.is_valid():
            expense = Expense.objects.create(date=datetime.now())
            for form in formset:
                if form.cleaned_data:
                    ExpenseEntry.objects.create(
                        expense=expense,
                        category=form.cleaned_data['category'],
                        amount=form.cleaned_data['amount']
                    )
            return redirect('home') 
    else:
        formset = ExpenseEntryFormSet()

    return render(request, 'add_expenses.html', {'formset': formset})
