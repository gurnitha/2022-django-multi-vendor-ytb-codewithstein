# apps/vendor/urls.py

# Django modules
from django.shortcuts import render

# Locals

def become_vendor(request):
    return render(request, 'vendor/become_vendor.html')


def vendor_admin(request):
    return render(request, 'vendor/vendor_admin.html')


def add_product(request):
    return render(request, 'vendor/add_product.html')


def vendor_login(request):
    return render(request, 'vendor/login.html')
