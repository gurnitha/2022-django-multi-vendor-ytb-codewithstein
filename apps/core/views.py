# apps/core/urls.py

# Django modules
from django.shortcuts import render

# Locals
from apps.product.models import Product

# Create your views here.


def frontpage(request):
    # Grab latest 8 products
    newest_products = Product.objects.all()[0:8]
    # print(newest_products)
    context = {
        'newest_products':newest_products
    }
    return render(request, 'core/frontpage.html', context)


def contact(request):
    return render(request, 'core/contact.html')