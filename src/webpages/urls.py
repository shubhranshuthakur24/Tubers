from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('aboutUs', views.aboutUs, name="aboutUs"),
    path('services', views.services, name="services"),
    path('contact', views.contact, name="contact"),
]
