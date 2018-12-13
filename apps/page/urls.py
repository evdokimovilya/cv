from django.urls import path
from apps.page import views

urlpatterns = [
    path('', views.index),
]
