from django.contrib import admin
from django.urls import path
from websiteAfter.views import websiteAfterHome

urlpatterns = [
    path("home1/",websiteAfterHome.home1,name="home1")
]