from django.db import models


class File(models.Model):
	name = models.SlugField('Название', max_length=60, unique=True)
	image = models.ImageField('Изображение', blank=True, null=True, upload_to='main')

	def __str__(self):
		return str(self.name)

	class Meta:
		verbose_name = 'Файл'
		verbose_name_plural = 'Файлы'
