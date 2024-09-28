from django.shortcuts import render
from .models import Homework

def homework_view(request):
    homework_data = Homework.objects.all()
    return render(request, 'homework/homework.html', {'homework_data': homework_data})