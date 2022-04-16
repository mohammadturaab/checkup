from django.urls import path
from . import views

urlspatterns = [
    path('', views.Home.as_view(), name="home")
]