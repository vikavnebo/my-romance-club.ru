from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.views.generic import DetailView, ListView
from stories.functions import create_breadcrumbs

from .models import *

menu = [
	{'title': "Истории", 'url_name': 'story_list'},
        {'title': "Об игре", 'url_name': 'about'},
        {'title': "Новости", 'url_name': 'new_list'}
]


def handler404(request, exception):
	context = {
		'menu': menu
	}
	return render(request, 'main/page_404.html', context=context, status=404)


def handler500(request):
	context = {
		'menu': menu
	}
	return render(request, 'main/page_500.html', context=context, status=500)


def get_about_page(request):
        context = {
                'menu': menu
        }
        return render(request, 'main/about.html', context=context)


class NewView(ListView):
	"""Список новостей"""
	model = New
	context_object_name = 'news'
	allow_empty = False
	paginate_by = 5

	def get_queryset(self):
		return New.objects.filter(draft=False)

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['menu'] = menu
		return context


class NewDetail(DetailView):
	"""Вывод конкретной истории"""
	model = New
	context_object_name = 'new'

	def get_queryset(self):
		return New.objects.filter(pk=self.kwargs['pk'], draft=False)

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)

		context['new_title'] = New.objects.get(pk=self.kwargs['pk'], draft=False).title

		titles = ('Новости', context['new_title'])
		urls = tuple(self.request.path[1:-1].split('/')[1:])

		context['breadcrumbs'] = create_breadcrumbs(titles, urls, path='/news/')
		context['menu'] = menu

		return context
