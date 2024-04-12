from django.core.management.base import BaseCommand
from ...models import AuthorModel
from django.utils import lorem_ipsum


class Command(BaseCommand):

	def handle(self, *args, **kwargs):
		for i in range(5):
			user = AuthorModel(name=f'Автор_{i}',
							   surname=f'Фамилия_{i}',
							   email=f'author{i}@tyt.ru',
							   bio=lorem_ipsum.words(10),
							   dob='1800-10-03')
			user.save()




