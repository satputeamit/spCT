from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=50)
    professor = models.CharField(max_length=50)
    description = models.TextField()
    student = models.ManyToManyField(Student, related_name="course")

    def __str__(self):
        return self.name





