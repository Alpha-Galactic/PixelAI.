from django.urls import path
from generator import views

urlpatterns = [
    path('', views.generate_image, name='generate_image'),
]