# apps/vendor/urls.py

# Django modules
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify

# Locals
from apps.vendor.models import Vendor


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


def vendor_admin(request):
    return render(request, 'vendor/vendor_admin.html')


def add_product(request):
    return render(request, 'vendor/add_product.html')


def vendor_login(request):
    return render(request, 'vendor/login.html')
