from django.db import models
# from course.models import Course
# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    code = models.PositiveSmallIntegerField()
    email = models.EmailField()
    age = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    next_of_kin = models.CharField(max_length=20)
    bio = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"