from django.contrib import admin
from django.urls import path, include

from .views import (home_view,login_view,confirm_logout_view,
                     register,add_expenses,generate_dataframe,
                     category_list,product_list,product_detail,
                     list_all_products,place_order,plotly_chart_view)
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
  path('', home_view,name='home'),
  path('login/', login_view, name='login'),
  path('confirm_logout/', confirm_logout_view, name='confirm_logout'),
  path('register/', register, name='register'),
  path('add_expenses/',add_expenses, name='add_expenses'),
  path('dataframe/', generate_dataframe, name='generate_dataframe'),
  path('chart/', plotly_chart_view, name='chart'),
  path('categories/', category_list, name='category_list'),
  path('products/<int:category_id>/', product_list, name='product_list'),
  path('products/', list_all_products, name='products_list'),
  path('product/<int:product_id>/', product_detail, name='product_detail'),
  path('order/<int:product_id>/', place_order, name='place_order'),




]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)