from django.contrib import admin
from django.urls import path, include

from .views import home_view, insert_json_data, harvest_data

urlpatterns = [
  path('home/', home_view,name='home'),
  path('insert_data/',insert_json_data, name='insert_data'),
  path('harvest_data/',harvest_data,name='harvest_data')


]