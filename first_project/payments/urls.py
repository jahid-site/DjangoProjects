from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='HomePage'),
    path('bkash/', views.bkash, name='Bkash'),
    
]
