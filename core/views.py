from django.shortcuts import render
from .models import Course
# Create your views here.

def courses(request):
    courses = Course.objects.all()
    return render(request, 'core/courses.html', {'courses': courses})
