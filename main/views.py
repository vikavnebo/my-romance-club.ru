from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.views.generic import DetailView, ListView
from .models import *


class NewView(ListView):
	"""Список новостей"""
	model = New
	context_object_name = 'news'
	allow_empty = False

	def get_queryset(self):
		return New.objects.filter(draft=False)


class NewDetail(DetailView):
	"""Вывод конкретной истории"""
	model = New
	context_object_name = 'news'

	def get_queryset(self):
		return New.objects.filter(pk=self.kwargs['pk'], draft=False)


def get_about_page(request):
	return render(request, 'main/about.html')


def page_not_found(request, exception):
	return HttpResponseNotFound(
		'''<h1>
		Страница не существует. Вы можете:
		- перейти в <a href="https://my-romance-club.ru/">каталог историй</a>
		- прочитать подробнее <a href="https://my-romance-club.ru/about">об игре</a>
		- узнать последние <a href="https://my-romance-club.ru/news">новости</a>
		</h1>''')
