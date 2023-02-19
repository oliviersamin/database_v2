from django.core.management import BaseCommand
import os


class Command(BaseCommand):
    help = "Test Telegram app to access to API endpoints"

    def handle(self, *args, **options):
        """
        """
        absolute_path_to_script = '/home/olivier/Documents/Projets/database/database/Telegram_app/basics/basic.py'
        os.system('python {}'.format(absolute_path_to_script))
