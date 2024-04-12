from django.core.management import BaseCommand
from seminarsapp.models import RandomDrops


class Command(BaseCommand):

	def handle(self, *args, **options):
		RandomDrops().save()
