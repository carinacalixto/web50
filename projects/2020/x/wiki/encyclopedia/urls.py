from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.entry, name="wiki"),
    path("wiki/", views.search, name="search")
]
