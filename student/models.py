from django.db import models
import os

def student_directory_name(instance,filename):
    return os.path.join('student/media', instance.name, filename)
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=150)
    checkbox = models.BooleanField()
    photo = models.ImageField(upload_to=student_directory_name,default=None,null=True)
    
    def __str__(self):
        return f"{self.name}"