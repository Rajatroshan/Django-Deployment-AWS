from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    rollNo = models.CharField(max_length=10)

    def __str__(self):
        return self.name
