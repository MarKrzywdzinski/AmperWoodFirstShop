from django.contrib import admin

# Register your models here.
from .models import Product, Kategoria, Portfolio

admin.site.register(Product)
admin.site.register(Kategoria)
admin.site.register(Portfolio)
