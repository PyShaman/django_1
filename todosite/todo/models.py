from django.db import models
from django.utils import timezone


class Todo(models.Model):
    objects = None
    producent = models.TextField(blank=True)
    wydawca = models.TextField(blank=True)
    tytul = models.TextField(blank=True)
    aktorzy = models.TextField(blank=True)
    scenarzysta = models.TextField(blank=True)
    kategoria = models.TextField(blank=True)
    ocena = models.CharField(max_length=3)
    status = models.TextField(blank=True)

    # title = models.CharField(max_length=100)
    # details = models.TextField()
    # date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
