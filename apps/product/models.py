# apps/product/models.py

# Django modules
from django.db import models
from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models

# Locals
from apps.vendor.models import Vendor

# Create your models here.


# Model: Category
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordering']
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(
    	Category, related_name='products', 
    	on_delete=models.CASCADE)
    vendor = models.ForeignKey(
    	Vendor, related_name='products', 
    	on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', 
    	blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', 
    	blank=True, null=True)

    class Meta:
        ordering = ['-date_added']
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return self.title
    
    # If product has no image, it will use this image
    def get_thumbnail(self):
    	# If added product has thumbnail, return this url
        if self.thumbnail:
            return self.thumbnail.url
        else:
        	# If added product has no thumbnail, generate image
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x180.jpg'
    
    # Make thumbnail
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail