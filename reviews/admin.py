from django.contrib import admin

from .models import Company, Category, Product, Review



for model in (Company, Category, Product, Review):
    admin.site.register(model)

