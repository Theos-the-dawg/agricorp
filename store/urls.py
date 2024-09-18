from django.contrib import admin
from django.urls import path, include

from .views import (home_view, insert_json_data, harvest_data,register)
from django.contrib.auth import views as auth_views
urlpatterns = [
  path('', home_view,name='home'),
  path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
  path('insert_data/',insert_json_data, name='insert_data'),
  path('harvest_data/',harvest_data,name='harvest_data'),
  path('register/', register, name='register'),



]