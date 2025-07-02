from rest_framework import viewsets
from rest_framework.response import Response
from .models import Course
from .serializers import CourseSerializer
# Create your views here.


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('course_id')
    serializer_class = CourseSerializer
    

