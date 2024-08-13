from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    code = models.PositiveSmallIntegerField(unique=True)  
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    salary = models.BigIntegerField()
    hire_date = models.DateTimeField()
    gender = models.CharField(max_length=10)
    bio = models.TextField()
    pic = models.ImageField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    

