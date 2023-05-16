from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="index"),
    path("shop/", shop, name="shop"),
    path("product-single/", product_single, name="product_single"),
    path("cart/", cart, name="cart"),
    path("checkout/", checkout, name="checkout"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
]