from django.core.management import BaseCommand
from seminarsapp.models import ArticleModel, AuthorModel, Comment


class Command(BaseCommand):
	def handle(self, *args, **options):
		author = AuthorModel.objects.filter(pk=4)[0]
		art = ArticleModel.objects.filter(pk=3)[0]
		# some_comm = Comment.objects.filter(article=art).first()

		# print(author.my1.count())



		# [Comment.objects.filter(pk=i).delete() for i in range(13,15)]

