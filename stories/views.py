from django.views.generic import DetailView, ListView
from django.db.models import Count
from .functions import create_breadcrumbs

from .models import *
from main.views import menu


class StoryView(ListView):
	"""Список историй"""
	model = Story
	context_object_name = 'stories'
	ordering = '-date'
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['menu'] = menu
		return context


class CharacterView(ListView):
	"""Список персонажей"""
	model = Character
	context_object_name = 'characters'

	def get_queryset(self):
		story_url = self.kwargs['story']
		queryset = Character.objects.filter(story__url=story_url)
		return queryset.annotate(scene_count=Count('scene')).order_by('-scene_count')

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)

		context['story_name'] = Story.objects.get(url=self.kwargs['story']).name
		context['story_url'] = Story.objects.get(url=self.kwargs['story']).url

		titles = ('Истории', context['story_name'])
		urls = tuple(self.request.path[1:-1].split('/'))

		context['breadcrumbs'] = create_breadcrumbs(titles, urls)
		context['menu'] = menu

		return context


class SceneView(ListView):
	"""Список сцен"""
	model = Scene
	context_object_name = 'scenes'

	def get_queryset(self):
		character_url = self.kwargs['character']
		queryset = Scene.objects.filter(character__url=character_url)
		return queryset.order_by('scene_number', 'name')

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)

		context['story_name'] = Story.objects.get(url=self.kwargs['story']).name
		context['character_name'] = Character.objects.get(url=self.kwargs['character']).name

		titles = ('Истории', context['story_name'], context['character_name'])
		urls = tuple(self.request.path[1:-1].split('/'))

		context['breadcrumbs'] = create_breadcrumbs(titles, urls)
		context['menu'] = menu

		return context

