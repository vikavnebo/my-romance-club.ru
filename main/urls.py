from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page


urlpatterns = [
	path('news/', NewView.as_view(), name='new_list'),
	path('news/<int:pk>/', NewDetail.as_view(), name='new_detail'),
	path('about/', get_about_page, name='about')
]
