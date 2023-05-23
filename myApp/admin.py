from django.contrib import admin
from .models import Carousel, Product, Brand, Category, SubCategory

# Register your models here.
admin.site.register(Carousel),
admin.site.register(Product),
admin.site.register(Category),
admin.site.register(SubCategory),
admin.site.register(Brand)