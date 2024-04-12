from django.core.management.base import BaseCommand
from ...models import User


class Command(BaseCommand):
	help = "Get user by id."

	def add_arguments(self, parser):
		parser.add_argument('id', type=int, help='User ID')
		# parser.add_argument('pk', type=int, help='User ID')

	def handle(self, *args, **kwargs):
		id = kwargs['id']
		user = User.objects.get(id=id)
		# pk = kwargs['pk']
		# user = User.objects.filter(pk=pk)
		self.stdout.write(f'{user}')
"""
Помимо оператора __gt существуют множество других. Перечислим
некоторые часто используемые:
● exact - точное совпадение значения поля
● iexact - точное совпадение значения поля без учета регистра
● contains - значение поля содержит заданный подстроку
● icontains - значение поля содержит заданный подстроку без учета
регистра
● in - значение поля находится в заданном списке значений
● gt - значение поля больше заданного значения
● gte - значение поля больше или равно заданному значению
● lt - значение поля меньше заданного значения
● lte - значение поля меньше или равно заданному значению
● startswith - значение поля начинается с заданной подстроки
● istartswith - значение поля начинается с заданной подстроки без учета
регистра
● endswith - значение поля заканчивается на заданную подстроку
● iendswith - значение поля заканчивается на заданную подстроку без
учета регистра
● range - значение поля находится в заданном диапазоне значений
● date - значение поля является датой, соответствующей заданной дате
● year - значение поля является годом, соответствующим заданному году"""