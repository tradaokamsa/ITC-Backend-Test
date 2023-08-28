from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("officers", views.officers, name="officers"),
    path("officers/<int:pl>", views.officers_detail, name="officers_detail"),
]