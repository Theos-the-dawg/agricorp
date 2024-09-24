from django.contrib import admin
from django.urls import path, include

from .views import (home_view, register,add_expenses,generate_dataframe)
from django.contrib.auth import views as auth_views
urlpatterns = [
  path('', home_view,name='home'),
  path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(template_name='confirm_logout.html'), name='logout'),
  path('register/', register, name='register'),
  path('add_expenses/',add_expenses,name='add_expenses'),
  path('dataframe/', generate_dataframe, name='generate_dataframe'),



]