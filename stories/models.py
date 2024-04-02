from django.db import models
from django.urls import reverse
from datetime import date
from .functions import *


class Genre(models.Model):
	"""Жанр истории: комедия, драма, ужасы и др."""
	name = models.CharField('Жанр', max_length=100, unique=True)
	url = models.SlugField('url', max_length=100, unique=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Жанр'
		verbose_name_plural = 'Жанры'


class ReleaseStatus(models.Model):
	"""Статус выхода истории: завершенные, незавершенные"""
	name = models.CharField('Статус', max_length=100, unique=True, default='Выпуск завершен')
	url = models.SlugField('url', max_length=100, unique=True, default='completed')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Статус выпуска'
		verbose_name_plural = 'Статусы выпуска'


class RelationshipType(models.Model):
	"""Тип отношений с персонажем: дружеские, романтические"""
	name = models.CharField('Отношения', max_length=100, unique=True, default='Любовная линия')
	url = models.SlugField('url', max_length=100, unique=True, default='beloved')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Тип отношений'
		verbose_name_plural = 'Типы отношений'


class Story(models.Model):
	"""Объект истории"""
	name = models.CharField('История', max_length=160, unique=True)
	url = models.SlugField('url', max_length=160, unique=True)
	date = models.DateField('Дата выхода', default=date.today)
	status = models.ForeignKey(ReleaseStatus, verbose_name='Статус выпуска',
	                           null=True, on_delete=models.DO_NOTHING)
	genre = models.ManyToManyField(Genre, verbose_name='Жанр')
	image = models.ImageField('Обложка', blank=True, null=True,
	                           upload_to=create_story_path)

	def __str__(self):
		return self.url
	
	def get_absolute_url(self):
		return reverse('character_list', kwargs={'story': self.url})

	class Meta:
		verbose_name = 'История'
		verbose_name_plural = 'Истории'
		ordering = ['name']


class Character(models.Model):
	"""Объект персонажа"""
	name = models.CharField('Имя', max_length=120)
	url = models.SlugField('url', max_length=120, unique=True)
	story = models.ForeignKey(Story, verbose_name='История', on_delete=models.CASCADE, null=True)
	relationship = models.ManyToManyField(RelationshipType, verbose_name='Отношения')
	image = models.ImageField('Изображение', blank=True, null=True,
	                          upload_to=create_character_path)

	def __str__(self):
		return self.url

	def get_absolute_url(self):
		return reverse('scene_list', kwargs={'story': self.story.url, 'character': self.url})

	class Meta:
		verbose_name = 'Персонаж'
		verbose_name_plural = 'Персонажи'
		ordering = ['story__name', 'name']


class Scene(models.Model):
	"""Объект кадра из истории"""
	name = models.CharField('Имя', max_length=120, default='Сцена c ')
	story = models.ForeignKey(Story, verbose_name='История', on_delete=models.CASCADE)
	character = models.ForeignKey(Character, verbose_name='Персонаж',
	                              on_delete=models.CASCADE, null=True)
	season = models.IntegerField('Сезон', default=1)
	chapter = models.IntegerField('Серия', default=1)
	scene_number = models.IntegerField('Номер сцены', default=1)
	image = models.ImageField('Изображение', blank=True, null=True,
	                          upload_to=create_scenes_path)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Кат-сцена'
		verbose_name_plural = 'Кат-сцены'
		ordering = ['story__name', 'character__name', 'id']
