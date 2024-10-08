from django.contrib import admin

from .models import Product, Owner

admin.site.register(Product)
admin.site.register(Owner)