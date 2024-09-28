from django.shortcuts import render
from .models import Attendance

def attendance_view(request):
    attendance_data = Attendance.objects.all()
    return render(request, 'attendance/attendance.html', {'attendance_data': attendance_data})