from django.db import models

class Homework(models.Model):
    student_name = models.CharField(max_length=255)
    class_name = models.CharField(max_length=255)
    assignment_name = models.CharField(max_length=255)
    due_date = models.DateField()
    status = models.CharField(max_length=10, choices=[('completed', 'Completed'), ('incomplete', 'Incomplete')])

    def __str__(self):
        return f'{self.student_name} - {self.class_name} - {self.assignment_name}'