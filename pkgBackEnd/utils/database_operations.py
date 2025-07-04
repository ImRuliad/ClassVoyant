from core.models import Course, Semester, CourseOfferings
import logging

def save_course_to_database(course_code: str, course_title: str, course_units: int) -> None:
    Course.objects.update_or_create(
        course_id=course_code,
        defaults={
            "course_title": course_title,
            "units": course_units
        }
    )

def save_semester_to_database(semester_name: str) -> None:
    Semester.objects.update_or_create(
        semester_name=semester_name
    )

def save_course_offerings_to_database(course_id: str, semester_name: str) -> None:
    semester = Semester.objects.get(semester_name=semester_name)
    course = Course.objects.get(course_id=course_id)
    
    CourseOfferings.objects.update_or_create(
        course_id=course,
        term_id=semester
    )