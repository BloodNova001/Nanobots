from django.db import models

class Attendance(models.Model):
    student_name = models.CharField(max_length=255)
    class_name = models.CharField(max_length=255)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent'), ('late', 'Late')])