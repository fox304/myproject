from django.core.management import BaseCommand
from seminarsapp.models import RandomDrops


class Command(BaseCommand):

	def handle(self, *args, **options):
		a = RandomDrops.amount_drops(6)
		self.stdout.write(f'{a}')

