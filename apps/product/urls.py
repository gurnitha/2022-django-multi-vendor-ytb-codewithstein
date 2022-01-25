# apps/product/urls.py

# Django modules
from django.urls import path

# Locals
from apps.product import views

app_name = 'product'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('product/', views.product, name='product'),
    path('category/', views.category, name='category'),
]