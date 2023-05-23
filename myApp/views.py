from django.shortcuts import render
from .models import Carousel, Product


def home(request):
    product = Product.objects.all()
    context = {"title": "Shoe Attic", "image": Carousel.objects.all(), "products": product}
    return render(request, "index.html", context)


def category(request):
    context = {"products": Product.objects.all()}
    return render(request, 'category.html', context)


def single_product(request):
    return render(request, template_name="single_product.html")


def cart(request):
    return render(request, template_name="cart.html")


def checkout(request):
    return render(request, template_name="checkout.html")


def about(request):
    return render(request, template_name="about.html")


def contact(request):
    return render(request, template_name="contact.html")

