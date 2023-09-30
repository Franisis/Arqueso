from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('registerUsers/', views.registers_userView, name = 'registers_user')
]