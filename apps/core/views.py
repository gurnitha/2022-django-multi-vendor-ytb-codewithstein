# apps/core/urls.py

# Django modules
from django.shortcuts import render

# Locals

def frontpage(request):
    return render(request, 'core/frontpage.html')


def contact(request):
    return render(request, 'core/contact.html')