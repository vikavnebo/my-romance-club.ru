from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.views.generic import DetailView, ListView
from .models import *


def page_not_found(request, exception):
	return render(request, 'main/page_404.html')


def get_about_page(request):
	return render(request, 'main/about.html')


class NewView(ListView):
	"""Список новостей"""
	model = New
	context_object_name = 'news'
	allow_empty = False
	paginate_by = 5

	def get_queryset(self):
		return New.objects.filter(draft=False)


# class NewDetail(DetailView):
# 	"""Вывод конкретной истории"""
# 	model = New
# 	context_object_name = 'new'
#
# 	def get_queryset(self):
# 		return New.objects.filter(pk=self.kwargs['pk'], draft=False)
#
# 	def get_context_data(self, *, object_list=None, **kwargs):
# 		context = super().get_context_data(**kwargs)
#
# 		context['new_title'] = New.objects.get(pk=self.kwargs['pk'], draft=False).title
#
# 		context['breadcrumbs'] = (
# 			{'name': 'Новости', 'url': f"/news"},
# 			{'name': context['new_title'], 'url': f"/news/{self.kwargs['pk']}"},
# 		)
# 		return context
