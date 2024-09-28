from django.shortcuts import render
from .models import StudentProfile

def student_profiles_view(request):
    student_profiles_data = StudentProfile.objects.all()
    return render(request, 'student_profiles/student_profiles.html', {'student_profiles_data': student_profiles_data})