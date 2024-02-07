from django.views.generic import DetailView, ListView
from django.db.models import Count
from .models import *


class StoryView(ListView):
	"""Список историй"""
	model = Story
	context_object_name = 'stories'
	ordering = '-date'


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

		context['breadcrumbs'] = (
			{"name": "Истории", "url": ""},
			{"name": context['story_name'], "url": f"/{context['story_url']}"},
		)
		return context


class SceneView(ListView):
	"""Список сцен"""
	model = Scene
	context_object_name = 'scenes'

	def get_queryset(self):
		character_url = self.kwargs['character']
		queryset = Scene.objects.filter(character__url=character_url)
		return queryset.order_by('name')

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)

		context['story_name'] = Story.objects.get(url=self.kwargs['story']).name
		context['character_name'] = Character.objects.get(url=self.kwargs['character']).name

		context['breadcrumbs'] = (
			{"name": "Истории", "url": ""},
			{"name": context['story_name'], "url": f"/{self.kwargs['story']}"},
			{"name": context['character_name'], "url": f"/{self.kwargs['story']}/{self.kwargs['character']}"},
		)
		return context
