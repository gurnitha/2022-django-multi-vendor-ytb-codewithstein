# apps/product/urls.py

# Django modules
from django.shortcuts import render

# Locals

def search(request):
    return render(request, 'product/search.html')


def product(request):
    return render(request, 'product/product.html')


def category(request):
    return render(request, 'product/category.html')