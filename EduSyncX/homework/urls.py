from django.urls import path
from . import views

urlpatterns = [
    path('', views.homework_view, name='homework'),
]