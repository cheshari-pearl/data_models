from django.db import models
from teacher.models import Teacher
from student.models import Student

class Classroom(models.Model):
    class_name = models.CharField(max_length=20)
    class_capacity = models.PositiveSmallIntegerField()
    class_duration = models.TimeField()
    class_ta = models.CharField(max_length=20)
    class_rep = models.CharField(max_length=20)
    class_empty_slots = models.SmallIntegerField()
    chair_numbers = models.PositiveSmallIntegerField()
    tables_numbers = models.PositiveSmallIntegerField()
    tv_numbers = models.PositiveSmallIntegerField()
    class_code = models.PositiveSmallIntegerField()
  

    first_name = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    first_name = models.OneToOneField(Student,on_delete=models.CASCADE)

    period_title = models.ForeignKey('classperiod.ClassPeriod', on_delete=models.CASCADE, related_name='period_name', default=2)