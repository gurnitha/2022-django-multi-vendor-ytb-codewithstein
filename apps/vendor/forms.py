# apps/vendor/forms.py

# Django modules
from django.forms import ModelForm

# Locals
from apps.product.models import Product

# Create your forms here.


# Form: ProductForm
class ProductForm(ModelForm):
	class Meta:
		model = Product 
		fields = ['category', 'image', 'title', 'description', 'price']