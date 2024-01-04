from django.urls import path
from .views import *


urlpatterns = [
	path('news/', get_news_page, name='news'),
	path('about/', get_about_page, name='about')
]
