from django.urls import path
from .views import home, category, single_product, cart, checkout, about, contact
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", home, name="index"),
    path("single-product/", single_product, name="single_product"),
    path("checkout/", checkout, name="checkout"),
    path("category/", category, name="category"),
    path("cart/", cart, name="cart"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)