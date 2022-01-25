# apps/vendor/urls.py

# Django modules
from django.urls import path
from django.contrib.auth import views as auth_views

# Locals
from apps.vendor import views

app_name = 'vendor'

urlpatterns = [
    path('become-vendor/', views.become_vendor, name='become_vendor'),
    path('vendor-admin/', views.vendor_admin, name='vendor_admin'),
    path('add-product/', views.add_product, name='add_product'),

    # Login and Logout

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='vendor/login.html'), name='login'),
]