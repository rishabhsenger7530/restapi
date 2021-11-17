from django.contrib import admin
from django.urls import path, include
from genericapi import views

urlpatterns = [
    path('',views.Home.as_view(), name = "home"),
    path('homeupdate/<int:pk>',views.HomeUpdate.as_view(), name = "homeupdate")
]
