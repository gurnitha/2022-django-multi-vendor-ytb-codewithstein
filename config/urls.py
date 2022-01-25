# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Core
    path('', include('apps.core.urls', namespace='core')),

    # Product
    path('', include('apps.product.urls', namespace='product')),

    # Vendor
    path('', include('apps.vendor.urls', namespace='vendor')),
]


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('vendors/', include('apps.vendor.urls')),
    
#     path('', include('apps.product.urls'))
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
