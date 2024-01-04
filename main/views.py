from django.shortcuts import render
from django.http import HttpResponseNotFound


def get_news_page(request):
	return render(request, 'main/news.html')


def get_about_page(request):
	return render(request, 'main/about.html')


def page_not_found(request, exception):
	return HttpResponseNotFound(
		'''<h1>
		Страница не существует. Вы можете:
		- перейти в <a href="{% url 'stories' %}">каталог историй</a>
		- прочитать подробнее <a href="{% url 'about' %}">об игре</a>
		- узнать последние <a href="{% url 'news' %}">новости</a>
		</h1>''')
