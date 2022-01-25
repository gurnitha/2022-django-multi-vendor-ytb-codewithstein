# config/urls.py

# Django modules
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Core
    path('', include('apps.core.urls', namespace='core')),

    # Product
    path('', include('apps.product.urls', namespace='product')),

    # Vendor
    path('', include('apps.vendor.urls', namespace='vendor')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

