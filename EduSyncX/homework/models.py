from django.db import models

class Homework(models.Model):
    assignment_name = models.CharField(max_length=255)
    due_date = models.DateField()
    class_name = models.CharField(max_length=255, default='Unknown')