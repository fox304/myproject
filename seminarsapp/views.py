from django.http import HttpResponse
from django.shortcuts import render, redirect
import random

from django.views import View
from django.views.generic import TemplateView

from seminarsapp.forms import SelectRandom, NewAuthor, NewAuthor2, NewArticle2
from seminarsapp.models import ArticleModel, AuthorModel


def random_number(request):
    return HttpResponse(f'<h1>случайное число от 0 до 100</h1><h3>{random.randrange(101)}</h3>')


def random_dice(request):
    return HttpResponse(f'<h1>на кубике выпало </h1><h3>{random.randrange(1, 7)}</h3>')


def random_coin(request):
    return HttpResponse(f'<h1>выпала монетка </h1><h3>{random.choice(["Орел", "Решка"])}</h3>')


def decor_for_random(func):
    #  декоратор для наших монет, костей, чисел
    def wrap(*args, **kwargs):
        return func(*args, **kwargs)

    return wrap


@decor_for_random
def random_number2(request):
    ran_num = [random.randrange(101) for i in range(5)]
    context = {
        'random_num': ran_num,
        'name': 'случайный номер от 1 до 100'
    }
    return render(request, 'seminarsapp/index1.html', context)


@decor_for_random
def random_dice2(request):
    ran_dice = [random.randrange(1, 7) for i in range(5)]
    context = {
        'random_num': ran_dice,
        'name': 'выпал кубик'
    }
    return render(request, 'seminarsapp/index1.html', context)


@decor_for_random
def random_coin2(request):
    ran_coin = [random.choice(["Орел", "Решка"]) for i in range(5)]
    context = {
        'random_num': ran_coin,
        'name': 'монетка выпала'
    }
    return render(request, 'seminarsapp/index1.html', context)


def random_all(request):
    if request.method == 'POST':
        form = SelectRandom(request.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            if game == 'coin': return random_coin2(request)
            if game == 'dice': return random_dice2(request)
            if game == 'number': return random_number2(request)
            print('валидация прошла успешно')
    else:
        form = SelectRandom()
        print('нужно заполнить форму')

    return render(request, 'seminarsapp/random_all.html',
                  {'form': form, 'name': 'случайные числа,монетка и кость'})


class AAA(TemplateView):
    """пробный класс"""
    template_name = 'seminarsapp/index3.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["n1"] = 1234567
        return context


def view_title_articls(request, id_author):
    art = ArticleModel.objects.filter(author=id_author)
    context = {
        "name": 'Список статей',
        "art": art
    }
    return render(request, 'seminarsapp/view_art.html', context)


def view_articl(request, id_article):
    art = ArticleModel.objects.get(pk=id_article)
    art.view_count += 1  # счетчик просмотров
    art.save()
    com = art.my.all().order_by('-changed_date')
    text = {
        "name": 'статья',
        'art': art,
        'com': com,
    }
    return render(request, 'seminarsapp/article.html', context=text)


def new_author_form(request):
    # descrip = 'не получилось добавить модель в БД'
    # if request.method == 'POST':
    # 	form = NewAuthor(request.POST)
    # 	if form.is_valid():
    # 		name = form.cleaned_data['name']
    # 		surname = form.cleaned_data['surname']
    # 		email = form.cleaned_data['email']
    # 		bio = form.cleaned_data['bio']
    # 		dob = form.cleaned_data['dob']
    #
    # 		AuthorModel.objects.create(name=name,
    # 									surname=surname,
    # 									email=email,
    # 									bio=bio,
    # 									dob=dob)
    # 		descrip  = 'мы добавили модель автора в БД'
    #
    # else:
    # 	form = NewAuthor()
    # return render(request,
    # 			  'seminarsapp/new_author_form.html',
    # 			  {'form': form, 'descrip': descrip})
    if request.method == 'POST':
        form = NewAuthor2(request.POST)
        if form.is_valid():
            # k = form.save()
            return redirect('ran')
        else:
            return random_dice2(request=request)
    return render(request, 'seminarsapp/new_author_form.html',
                  {'form': NewAuthor2()})


def new_article_form(request):
    form = NewArticle2()
    if request.method == 'POST':
        authors = AuthorModel.objects.all()
        author = random.choice(authors)
        form = NewArticle2(request.POST)
        if form.is_valid():

            form.author = author
            form.save()
            print(form.author)
        else:
            form = NewArticle2(request.POST)

    return render(request, 'seminarsapp/new_article_form.html', {'form': form})
