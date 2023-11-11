from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('results/', views.get_results), 
    path('resultCreate/', csrf_exempt(views.createResults, name = 'createResults'))
    
]

