from time import sleep

from django.core.management import BaseCommand
from django.utils import lorem_ipsum
import random
from seminarsapp.models import ArticleModel, AuthorModel, Comment


class Command(BaseCommand):
	def handle(self, *args, **options):
		authors = AuthorModel.objects.all()
		articles = ArticleModel.objects.all()

		for _ in range(20):
			comment = " ".join(lorem_ipsum.paragraphs(4))
			Comment(


				article=random.choice(articles),

				author=random.choice(authors),

				text=comment,
			).save()
			sleep(2)

	# Comment.objects.all().delete()
