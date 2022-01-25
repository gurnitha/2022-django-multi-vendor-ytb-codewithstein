# apps/vendor/urls.py

# Django modules
from django.urls import path
from django.contrib.auth import views as auth_views

# Locals
from apps.vendor import views

app_name = 'vendor'

urlpatterns = [
    path('vendor/become-vendor/', views.become_vendor, name='become_vendor'),
    path('vendor/vendor-admin/', views.vendor_admin, name='vendor_admin'),
    path('vendor/add-product/', views.add_product, name='add_product'),

    # Login and Logout
    path('vendor/logout', auth_views.LogoutView.as_view(), name='logout'),
    path('vendor/login/', views.vendor_login, name='vendor_login'),
]