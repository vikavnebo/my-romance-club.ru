from django.views.generic import DetailView, ListView
from .models import *


class StoryView(ListView):
	"""Список историй"""
	model = Story
	queryset = Story.objects.all().order_by('-date')
	context_object_name = 'stories'


class CharacterView(ListView):
	"""Список персонажей конкретной истории"""
	model = Character
	context_object_name = 'characters'
	slug_field = 'story'

	def get_queryset(self):
		queryset = super().get_queryset()
		story = self.kwargs['story']
		queryset = queryset.filter(story__url=story)
		return queryset


class CharacterDetailView(DetailView):
	"""Страница персонажа"""
	model = Character
	slug_field = 'url'
	slug_url_kwarg = 'url'

	def get_queryset(self):
		return super().get_queryset().select_related('story')
