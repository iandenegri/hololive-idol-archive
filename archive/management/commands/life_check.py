# Local
from tickers.utils import TickersImport

# Django
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Goes through all videos in the database and checks if the video is still available. If not, we set the video to private on our DB"
    def handle(self, *args, **options):
        # Get all videos
        # Start iterating through videos

        return True
