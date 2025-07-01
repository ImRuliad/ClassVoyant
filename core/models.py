from django.db import models

# Create your models here.

class Course(models.Model):
    course_id = models.CharField(max_length=10, primary_key=True)
    course_title = models.CharField(max_length=200)
    units = models.IntegerField()

    def __str__(self):
        return f"{self.course_id}: {self.course_title}"

class Semester(models.Model):
    semester_name = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return f"{self.semester_name}"