from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
    objects = models.Manager() # is a default manager of every model in django

    def __str__(self):      # is a special method of python to determine what to print when a Task object is printed
        return self.title