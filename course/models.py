from django.db import models

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
    name = models.CharField(max_length=20)

    name = models.ForeignKey('student.Student', on_delete=models.CASCADE, related_name='courses' , default='default_first_name')
    first_name = models.OneToOneField('teacher.Teacher', on_delete=models.CASCADE, related_name='course')
    