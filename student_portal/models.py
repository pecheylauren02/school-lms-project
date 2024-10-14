from django.db import models
from django.contrib.auth.models import User


class Grade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    score = models.FloatField()

    def __str__(self):
        return f"{self.subject}: {self.score}"


class Timetable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(max_length=10)
    subject = models.CharField(max_length=100)
    time = models.TimeField()

    def __str__(self):
        return f"{self.day}: {self.subject} at {self.time}"
