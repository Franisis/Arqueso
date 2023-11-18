from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('results', views.resultGet, name = 'resultGet'),
    path('resultsCreate', csrf_exempt(views.resultPost), name = 'resultPost',  ),
    
]
