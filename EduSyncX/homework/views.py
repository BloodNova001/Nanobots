from django.shortcuts import render, redirect
from .models import Homework
from .forms import HomeworkForm

def homework_view(request):
    homework_data = Homework.objects.all().order_by('-id')
    return render(request, 'homework/homework.html', {'homework_data': homework_data})

def add_homework(request):
    if request.method == 'POST':
        form = HomeworkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homework')
    else:
        form = HomeworkForm()
    return render(request, 'homework/add_homework.html', {'form': form})

def view_homework(request, pk):
    homework = get_object_or_404(Homework, pk=pk)
    return render(request, 'homework/view_homework.html', {'homework': homework})

def edit_homework(request, id):
    homework = Homework.objects.get(id=id)
    if request.method == 'POST':
        form = HomeworkForm(request.POST, instance=homework)
        if form.is_valid():
            form.save()
            return redirect('homework')
    else:
        form = HomeworkForm(instance=homework)
    return render(request, 'homework/edit_homework.html', {'form': form})

def delete_homework(request, id):
    homework = Homework.objects.get(id=id)
    homework.delete()
    return redirect('homework')