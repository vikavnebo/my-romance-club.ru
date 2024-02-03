from django.db import models
from datetime import date


class NewsFile(models.Model):
	name = models.SlugField('Название', max_length=60, unique=True)
	file = models.ImageField('Изображение', unique=True, blank=True, null=True, upload_to='main/news')

	def __str__(self):
		return str(self.name)

	class Meta:
		verbose_name = 'Файл'
		verbose_name_plural = 'Файлы'


class New(models.Model):
	title = models.CharField('Заголовок', max_length=120)
	text = models.TextField('Текст')
	date = models.DateField('Дата публикации', default=date.today)
	draft = models.BooleanField('Черновик', default=False)
	image = models.ForeignKey(NewsFile, to_field='file', on_delete=models.SET_NULL, blank=True, null=True)

	def __str__(self):
		return str(self.title)

	class Meta:
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'
		ordering = ['-date']

