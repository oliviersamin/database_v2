from django.core.management import BaseCommand
import os
import datetime


class Command(BaseCommand):
    help = "Test Telegram app to access to API endpoints"
    DATABASE_BACKUP_FOLDER_PATH = '/home/olivier/Desktop'
    BASE_BACKUP_NAME = 'database_backup'
    ORIGINAL_DATABASE = '/home/olivier/Documents/Projets/database_v2/db.sqlite3'


    def setup_db_name(self):
        now = datetime.datetime.now()
        month = '0' + str(now.month) if now.month < 10 else str(now.month)
        final_name = self.BASE_BACKUP_NAME + '_' + str(now.year) + month + str(now.day) + '.sqlite3'
        backup_path = os.path.join(self.DATABASE_BACKUP_FOLDER_PATH, final_name)
        return backup_path

    def handle(self, *args, **options):
        """
        """
        print('=' * 50 + ' STARTING SAVING DATABASE ' + '=' * 50)
        FULL_BACKUP_PATH = self.setup_db_name()
        BACKUP_COMMAND = 'sqlite3 {} ".backup {}"'.format(self.ORIGINAL_DATABASE, FULL_BACKUP_PATH)
        os.system(BACKUP_COMMAND)
        print('=' * 50 + ' DATABASE SAVED' + '=' * 50)
