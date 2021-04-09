from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length = 200)
    RegistrationNumber = models.CharField(max_length = 200)
    CourseUnit = models.CharField(max_length = 200)
    Marks = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.RegistrationNumber