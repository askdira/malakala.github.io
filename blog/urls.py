from django.urls import path
from . import views

urlpatterns = [
    path('', views.indeks, name='indeks'),
    path('<int:pk>/', views.detail, name='detail'),
]