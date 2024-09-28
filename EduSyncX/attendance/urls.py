from django.urls import path
from . import views

urlpatterns = [
    path('', views.attendance_view, name='attendance'),
    path('all_attendance/', views.all_attendance_view, name='all_attendance'),
    path('delete_attendance/<int:id>/', views.delete_attendance, name='delete_attendance'),
    path('edit_attendance/<int:id>/', views.edit_attendance, name='edit_attendance'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]