from django.urls import path, include
from rest_framework import routers
from core.views import CourseViewSet


router = routers.DefaultRouter()
router.register(r'api/courses', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]