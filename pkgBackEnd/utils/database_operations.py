from core.models import Course
import logging

@staticmethod
def save_course_to_database(course_code: str, course_title: str, course_units: str) -> None:
    Course.objects.update_or_create(
        course_id=course_code,
        defaults={
            "course_title": course_title,
            "units": course_units
        }
    )