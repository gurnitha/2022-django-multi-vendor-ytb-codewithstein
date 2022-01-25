# apps/vendor/urls.py

# Django modules
from django.urls import path

# Locals
from apps.vendor import views

app_name = 'vendor'

urlpatterns = [
    path('vendor/become-vendor/', views.become_vendor, name='become_vendor'),
    path('vendor/vendor-admin/', views.vendor_admin, name='vendor_admin'),
    path('vendor/add-product/', views.add_product, name='add_product'),
    path('vendor/login/', views.vendor_login, name='vendor_login'),
]