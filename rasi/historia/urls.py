from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    
    path('histories/', views.get_historias, name = 'historyGet'),
    path('registerHistory/', views.create_historia, name ="historyCreate"),
    path('pageUpdateHistory/', csrf_exempt(views.createHistoryPage), name='createHistoryPage'),
    path('updateHistory/', csrf_exempt(views.update_history_reason), name="historyUpdate"),
     path('showAllHistories/', views.show_all_histories, name='showAllHistories'),

]