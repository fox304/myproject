import random
from time import sleep

import names
from django.core.management import BaseCommand

from seminarsapp.models import ArticleModel,AuthorModel,Comment


class Command(BaseCommand):
	def handle(self, *args, **options):
		rand = Comment.objects.all()
		for i in range(10):
			comm = random.choice(rand)
			comm.text = names.get_full_name()
			comm.save()
			sleep(2)

		# comm.update(text='первое изменение')
		# self.stdout.write(f'{comm[0].text}')

