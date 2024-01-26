from django.contrib import admin
from stories.models import *


class StoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'url', 'image')
	list_display_links = ('name', 'url')
	search_fields = ('name', 'url')
	list_editable = ('image',)
	list_filter = ('status', 'genre')


class CharacterAdmin(admin.ModelAdmin):
        list_display = ('name', 'url', 'story', 'image')
        list_display_links = ('name', 'url')
        search_fields = ('name', 'url', 'story')
        list_editable = ('story', 'image')
        list_filter = ('story',)


class SceneAdmin(admin.ModelAdmin):
        list_display = ('name', 'story', 'character', 'image')
        list_display_links = ('name',)
        search_fields = ('name', 'story', 'character')
        list_editable = ('story', 'character','image')
        list_filter = ('story', 'character')


admin.site.register(Genre)
admin.site.register(ReleaseStatus)
admin.site.register(RelationshipType)
admin.site.register(Story, StoryAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Scene, SceneAdmin)
