from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page


urlpatterns = [
	path('news/', cache_page(60 * 15)(NewView.as_view()), name='new_list'),
	path('news/<int:pk>/', cache_page(60 * 15)(NewDetail.as_view()), name='new_detail'),
	path('about/', get_about_page, name='about')
]
