# apps/product/urls.py

# Django modules
import random
from django.shortcuts import render, get_object_or_404


# Locals
from .models import Category, Product

# Create your views here.


def search(request):
    return render(request, 'product/search.html')


def product(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)

    similar_products = list(product.category.products.exclude(id=product.id))

    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products, 4)

    return render(request, 'product/product.html', {'product': product, 'similar_products': similar_products})

def category(request):
    return render(request, 'product/category.html')