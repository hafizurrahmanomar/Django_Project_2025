from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
# Compare this snippet from home/urls.py:
# from django.urls import path
