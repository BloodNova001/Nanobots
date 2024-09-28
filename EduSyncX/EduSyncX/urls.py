from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('attendance/', include('attendance.urls')),
    path('homework/', include('homework.urls')),
    path('announcements/', include('announcements.urls')),
    path('student_profiles/', include('student_profiles.urls')),
    path('dashboard/', include('dashboard.urls')),
]