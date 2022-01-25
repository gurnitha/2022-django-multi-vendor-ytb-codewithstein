# apps/core/urls.py

# Django modules
from django.urls import path

# Locals
from apps.core import views

app_name = 'core'

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('contact/', views.contact, name='contact'),
]