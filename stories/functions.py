def create_story_path(instance, filename):
	image_type = filename.split('.')[-1]
	story = instance.url
	filename = f'{story}.{image_type}'
	return f'stories/{story}/{filename}'


def create_character_path(instance, filename):
	image_type = filename.split('.')[-1]
	story = instance.story.url
	character = instance.url
	filename = f'{character}.{image_type}'
	return f'stories/{story}/{character}/{filename}'


def create_scenes_path(instance, filename):
	image_type = filename.split('.')[-1]
	story = instance.story.url
	character = instance.character.url
	number = instance.name.split()[-1]
#	number = instance.scene_number
	filename = f'{character}_{number}.{image_type}'
	return f'stories/{story}/{character}/scenes/{filename}'


def create_breadcrumbs(titles: tuple, urls: tuple, path='/') -> list:
	breadcrumbs = []
	i = 0
	for title in titles:
		item = {}
		if breadcrumbs:
			path += urls[i] + '/'
			i += 1
		item['name'] = title
		item['url'] = path
		breadcrumbs.append(item)
	return breadcrumbs
