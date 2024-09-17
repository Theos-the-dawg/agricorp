from django.views.decorators.csrf import csrf_exempt


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .utils import authenticate_custom_user,DateTimeEncoder
from django.http import HttpResponse
from django.contrib.auth import get_user_model,login,logout,get_user
from django.contrib.auth.models import User
import json
from .forms import HarvestForm
from .models import Harvest
#from docx import Document
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home_view(request):

    return render()


def about():
    pass

def harvest_data(request,data):
   
 pass

def insert_json_data(request):

 """ MODELL INSTANCE TO UP LOAD JSON DATA FROM EACH FIELD IN THE DATA TABLE MUST BE POPULATED!"""

pass

def contact():
    pass

