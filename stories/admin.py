from django.contrib import admin
from django.utils.safestring import mark_safe
from stories.models import *


class StoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'url', 'get_html_photo')
	list_display_links = ('name', 'url')
	search_fields = ('name', 'url')
	list_editable = ('image',)
	list_filter = ('status', 'genre')
	readonly_fields = ('get_html_photo',)
	fields = ('name', 'url', 'date', 'status', 'genre', 'image', 'get_html_photo')
	save_on_top = True

	def get_html_photo(self, object):
		if object.image:
			return mark_safe(f"<img src='{object.image.url}' width=50>")

	get_html_photo.short_description = 'Миниатюра'


class CharacterAdmin(admin.ModelAdmin):
        list_display = ('name', 'url', 'story', 'image')
        list_display_links = ('name', 'url')
        search_fields = ('name', 'url', 'story')
        list_editable = ('story', 'image')
        list_filter = ('story',)


class SceneAdmin(admin.ModelAdmin):
        list_display = ('name', 'scene_number', 'story', 'character', 'season', 'chapter', 'image')
        list_display_links = ('name',)
        search_fields = ('name', 'story', 'character')
        list_editable = ('scene_number', 'story', 'character', 'season', 'chapter', 'image')
        list_filter = ('story', 'character', 'season', 'chapter', 'scene_number')


admin.site.register(Genre)
admin.site.register(ReleaseStatus)
admin.site.register(RelationshipType)
admin.site.register(Story, StoryAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Scene, SceneAdmin)
