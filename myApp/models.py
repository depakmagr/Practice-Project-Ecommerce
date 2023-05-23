from django.db import models

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to="BrandImage", blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to="ProductImage", null=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Carousel(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=800, blank=True)
    image = models.ImageField(upload_to="bg_img/", null=True)

    def __str__(self):
        return self.name