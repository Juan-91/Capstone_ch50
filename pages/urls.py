from django.urls import path
from .views import home, about, contact, terms


urlpatterns = [
    path("", home, name="root"),
    path("home/", home, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("terms/", terms, name="terms")
]