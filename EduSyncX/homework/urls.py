from django.urls import path
from . import views

urlpatterns = [
    path('', views.homework_view, name='homework'),
    path('homework/add/', views.add_homework, name='add_homework'),
    path('homework/<int:pk>/', views.view_homework, name='view_homework'),
    path('edit_homework/<int:id>/', views.edit_homework, name='edit_homework'),
    path('delete_homework/<int:id>/', views.delete_homework, name='delete_homework'),
]