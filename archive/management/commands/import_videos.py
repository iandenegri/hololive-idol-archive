# Local
from tickers.utils import TickersImport

# Django
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Goes through all singers in the database and attempts to bring in any videos that aren't in the database."
    def handle(self, *args, **options):
        # Get all singers
        # Start iterating through singers
        # 

        return True
