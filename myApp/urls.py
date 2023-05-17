from django.urls import path
from .views import home, shop, single_product, cart, checkout, about, contact

urlpatterns = [
    path("", home, name="index"),
    path("shop/", shop, name="shop"),
    path("single-product/", single_product, name="single_product"),
    path("cart/", cart, name="cart"),
    path("checkout/", checkout, name="checkout"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
]