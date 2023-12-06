from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    
    path('histories/', views.get_historias, name = 'historyGet'),
    path('registerHistory/', views.create_historia, name ="historyCreate "),
    path('pageUpdateHistory/', views.create_history_page, name = 'createHistoryPage'),
    path('updateHistory/', views.update_history_reason, name="historyUpdate"),

]