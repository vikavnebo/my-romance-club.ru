from django.contrib import admin
from main.models import *


class NewAdmin(admin.ModelAdmin):
	list_display = ('title', 'date', 'draft', 'image')
	list_display_links = ('title',)
	search_fields = ('title',)
	list_editable = ('draft', 'image',)
	list_filter = ('date',)


admin.site.register(NewsFile)
admin.site.register(New, NewAdmin)

