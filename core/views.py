from rest_framework import viewsets
from rest_framework.response import Response
from .models import Semester, Course
from .serializers import SemesterSerializer, CourseSerializer
# Create your views here.

class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all().order_by('semester_name')
    serializer_class = SemesterSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('course_id')
    serializer_class = CourseSerializer
    

