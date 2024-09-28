from django.db import models

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f'{self.title} - {self.date}'