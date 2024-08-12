from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .utils import authenticate_custom_user,DateTimeEncoder
from django.http import HttpResponse
from django.contrib.auth import get_user_model,login,logout,get_user
from django.contrib.auth.models import User
import json
#from docx import Document
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home_view(request):
    user=list(User.objects.all())
    return render(request,user)
def about():
    pass

def services():
    pass

def contact():
    pass

