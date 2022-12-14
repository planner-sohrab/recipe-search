from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("specific/", views.specific, name="specific"),
    path("search/", views.search, name="search"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
