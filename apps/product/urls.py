# apps/product/urls.py

# Django modules
from django.urls import path

# Locals
from apps.product import views

app_name = 'product'

urlpatterns = [
    path('<slug:category_slug>/<slug:product_slug>/', views.product, name='product'),


    path('search/', views.search, name='search'),
    path('category/', views.category, name='category'),
]