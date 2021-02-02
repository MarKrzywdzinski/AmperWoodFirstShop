from django.contrib import admin

# Register your models here.
from .models import Product, Kategoria

admin.site.register(Product)
admin.site.register(Kategoria)
