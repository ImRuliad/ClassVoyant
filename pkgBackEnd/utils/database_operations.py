from core.models import Course, Semester
import logging

@staticmethod
def save_course_to_database(course_code: str, course_title: str, course_units: int) -> None:
    Course.objects.update_or_create(
        course_id=course_code,
        defaults={
            "course_title": course_title,
            "units": course_units
        }
    )

@staticmethod
def save_semester_to_database(semester_name: str) -> None:
    Semester.objects.update_or_create(
        semester_name=semester_name
    )