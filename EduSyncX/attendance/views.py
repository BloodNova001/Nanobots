from django.shortcuts import render, redirect
from .models import Attendance
from .forms import AttendanceForm

def attendance_view(request):
    attendance_data = Attendance.objects.all().order_by('-id')[:5]
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance')
    else:
        form = AttendanceForm()
    return render(request, 'attendance/attendance.html', {'attendance_data': attendance_data, 'form': form})

def all_attendance_view(request):
    attendance_data = Attendance.objects.all().order_by('-id')
    return render(request, 'attendance/all_attendance.html', {'attendance_data': attendance_data})

def delete_attendance(request, id):
    attendance = Attendance.objects.get(id=id)
    attendance.delete()
    return redirect('all_attendance')

def edit_attendance(request, id):
    attendance = Attendance.objects.get(id=id)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('all_attendance')
    else:
        form = AttendanceForm(instance=attendance)
    return render(request, 'attendance/edit_attendance.html', {'form': form})

def dashboard_view(request):
    return render(request, 'dashboard.html')