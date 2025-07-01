from django.shortcuts import render
from django.views.generic import ListView
from .models import Course
# Create your views here.


class CourseListView(ListView):
    model = Course
    template_name = 'core/courses.html'
    context_object_name = 'courses'
    ordering = ['course_id']


