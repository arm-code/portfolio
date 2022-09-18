from django.urls import path, include
from . import views

urlpatterns = [
    path('alexis', views.alexis, name="alexis")    
]