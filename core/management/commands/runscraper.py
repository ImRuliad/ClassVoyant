from django.core.management.base import BaseCommand
from django.conf import settings
import logging
from pkgBackEnd.setup.initialize import run_setup


class Command(BaseCommand):
    help = "Runs the course data scraper to fetch semester and major data from a user defined semester."

    def add_arguments(self, parser):
        parser.add_argument('semester_name', type=str, help='The name of the semester to scrape)')

    def handle(self, *args, **options):
        semester_name = options['semester_name']
        self.stdout.write(self.style.SUCCESS(f"Starting the scraper for semester: {semester_name}..."))

        if not settings.BASE_URL:
            self.stderr.write(self.style.ERROR("BASE_URL is not configured in settings. Exiting."))
            return

        try:
            run_setup(settings.BASE_URL, semester_name)
            self.stdout.write(self.style.SUCCESS("Scraper finished successfully."))
        except Exception as e:
            logging.exception("An error occurred during scraping.")
            self.stderr.write(self.style.ERROR(f"An error occurred during scraping: {e}"))