from django import forms
from .models import Homework

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ('assignment_name', 'due_date', 'class_name')