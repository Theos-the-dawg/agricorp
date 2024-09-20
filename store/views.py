from django.views.decorators.csrf import csrf_exempt


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .models import Harvest
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import HarvestForm,CustomUserCreationForm,LoginForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


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

@login_required
def logout_view(request):
 if request.method == 'POST':
        if 'confirm' in request.POST:
            # If the user confirmed, log them out
            logout(request)
            return redirect('home')  # Redirect to home or another page after logout
        else:
            # If the user clicked "Cancel", redirect them back to home or dashboard
            return redirect('home')  # You can change 'home' to your preferred URL
 return render(request, 'logout.html')

def harvest_data(request,data):
   
 pass

def insert_json_data(request):

 """ MODELL INSTANCE TO UP LOAD JSON DATA FROM EACH FIELD IN THE DATA TABLE MUST BE POPULATED!"""

pass

def contact():
    pass

