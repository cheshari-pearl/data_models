from django.db import models

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
    pic = models.ImageField()
    course_title = models.CharField(max_length=20)

    course_title = models.ManyToManyField('course.Course', related_name='students')

