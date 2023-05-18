from django.db import models

# Create your models here


class Carousel(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=800, blank=True)
    image = models.ImageField(upload_to="bg_img/", null=True)

    def __str__(self):
        return self.title