from django.views.decorators.csrf import csrf_exempt


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .models import Harvest
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import HarvestForm,CustomUserCreationForm
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
            login(request, user)  # Log the user in after successful registration
            return redirect('home')  # Redirect to home page or any other page
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})




def harvest_data(request,data):
   
 pass

def insert_json_data(request):

 """ MODELL INSTANCE TO UP LOAD JSON DATA FROM EACH FIELD IN THE DATA TABLE MUST BE POPULATED!"""

pass

def contact():
    pass

