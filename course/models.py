from django.db import models
from student.models import Student
from teacher.models import Teacher

class Course(models.Model):
    course_title = models.CharField(max_length=20)
    course_description = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    course_code = models.PositiveSmallIntegerField()
    teacher_code = models.PositiveSmallIntegerField()
    course_materials = models.TextField()
    course_attendees = models.PositiveSmallIntegerField()
    course_fee = models.CharField(max_length=20)
    first_name = models.ForeignKey(Student,on_delete=models.CASCADE, default=2)
    first_name=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.course_title} {self.course_description}"