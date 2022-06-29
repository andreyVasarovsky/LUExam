from django.db import models


class StudentModel(models.Model):
    name = models.CharField(max_length=200)
    grades = models.CharField(max_length=100)
    average_grade = models.FloatField()