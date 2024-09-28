from django.db import models

class StudentProfile(models.Model):
    student_name = models.CharField(max_length=255)
    class_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.student_name} - {self.class_name}'