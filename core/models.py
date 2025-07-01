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

class CourseOfferings(models.Model):
    offering_id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(Course, to_field="course_id", on_delete=models.CASCADE)
    term_id = models.ForeignKey(Semester, to_field="semester_name", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.offering_id}: {self.course_id} - {self.term_id}"