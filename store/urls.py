from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.confirm_logout_view, name='confirm_logout'),
    path('add-expenses/', views.add_expenses, name='add_expenses'),
    path('dataframe/', views.generate_dataframe, name='generate_dataframe'),
    path('chart/', views.plotly_chart_view, name='plotly_chart'),
    path('categories/', views.category_list, name='category_list'),
    path('products/', views.list_all_products, name='products_list'),
    path('category/<int:category_id>/products/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product/<int:product_id>/order/', views.place_order, name='place_order'),
    path('cart/', views.cart_logic, name='cart'),
    path('orders/', views.order_history, name='order_history'),
]
