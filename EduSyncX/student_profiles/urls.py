from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_profiles_view, name='student_profiles'),
]