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
   
   json_data = json.loads(data)
   my_instance = Harvest.objects.create(crops=json_data)
   my_instance = my_instance.save(commit=False)
   my_instance.save()
            
            # Perform additional operations
   #my_instance.additional_field = "Some additional data"
            
            # Save the instance to the database
    

def insert_json_data(request):
    if request.method == 'POST':
        form = HarvestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('some_view_name')
    else:
        form =HarvestForm()

    return render(request, 'insert_json_data.html', {'form': form})

\
def contact():
    pass

