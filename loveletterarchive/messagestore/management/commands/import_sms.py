from django.core.management.base import BaseCommand, CommandError
from messagestore.models import TextMessage
import xml.etree.ElementTree as ET


class Command(BaseCommand):
    help = 'Import SMS exported via XML from the app SMS Backup & Restore.'

    def add_arguments(self, parser):
        parser.add_argument('sms_file_name', type=str)

    def handle(self, *args, **options):
        with open(options['sms_file_name']) as file:
            print("Filename" + file.name)
            tree = ET.parse(file)
            root = tree.getroot()
            print('test')
