from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, template_name="index.html")


def shop(request):
    return render(request, template_name="shop.html")


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

