# apps/vendor/urls.py

# Django modules
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify

# Locals
from apps.vendor.models import Vendor
from apps.product.models import Category, Product

# Create your models here.


def become_vendor(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            vendor = Vendor.objects.create(
                name=user.username,
                created_by=user)

            return redirect('core:frontpage')

    else:
        form = UserCreationForm()

    context = {'form':form}

    return render(request, 'vendor/become_vendor.html', context)


@login_required
def vendor_admin(request):
    vendor = request.user.vendor # Refer to Vendor model => related_name='vendor'
    products = vendor.products.all()
    context = {
        'vendor':vendor,
        'products':products
    }
    return render(request, 'vendor/vendor_admin.html', context)


def add_product(request):
    return render(request, 'vendor/add_product.html')
