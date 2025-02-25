from django.contrib import admin
from django.urls import path, include

from .views import (home_view,login_view,confirm_logout_view, register,add_expenses,generate_dataframe)
from django.contrib.auth import views as auth_views
urlpatterns = [
  path('', home_view,name='home'),
  path('login/', login_view, name='login'),
  path('logout/', confirm_logout_view, name='logout'),
  path('register/', register, name='register'),
  path('add_expenses/',add_expenses,name='add_expenses'),
  path('dataframe/', generate_dataframe, name='generate_dataframe'),



]