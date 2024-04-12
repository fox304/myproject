from django.core.management.base import BaseCommand
from ...models import ArticleModel,AuthorModel
from django.utils import lorem_ipsum
import random

class Command(BaseCommand):

	def handle(self, *args, **kwargs):
		authors = AuthorModel.objects.all()
		for i in range(2):

			article = ArticleModel(author=random.choice(authors),
							       title=f'Статья № {i}',
							       text=lorem_ipsum.paragraphs(4),
							       category=f'Категория {i}',
								   publicated_flag=random.choice([True,False])
								   )
			article.save()
		# ArticleModel.objects.all().delete()
