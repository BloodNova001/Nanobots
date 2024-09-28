from django.shortcuts import render
from .models import Announcement

def announcements_view(request):
    announcements_data = Announcement.objects.all()
    return render(request, 'announcements/announcements.html', {'announcements_data': announcements_data})