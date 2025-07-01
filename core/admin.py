from django.contrib import admin
from .models import Course

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'course_title', 'units')
    search_fields = ('course_id', 'course_title')
    list_filter = ('units',)
    ordering = ('course_id',)
