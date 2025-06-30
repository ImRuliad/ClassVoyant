from django.core.management.base import BaseCommand
from django.conf import settings
import logging
from pkgBackEnd.setup.initialize import run_setup


class Command(BaseCommand):
    help = "Runs the course data scraper to fetch semester and major data."

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Starting the scraper..."))

        if not settings.BASE_URL:
            self.stderr.write(self.style.ERROR("BASE_URL is not configured in settings. Exiting."))
            return

        try:
            run_setup(settings.BASE_URL)
            self.stdout.write(self.style.SUCCESS("Scraper finished successfully."))
        except Exception as e:
            logging.exception("An error occurred during scraping.")
            self.stderr.write(self.style.ERROR(f"An error occurred during scraping: {e}"))