from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', cache_page(60 * 15)(StoryView.as_view()), name='story_list'),
    path('<slug:story>', cache_page(60 * 15)(CharacterView.as_view()), name='character_list'),
    path('<slug:story>/<slug:character>', cache_page(60 * 15)(SceneView.as_view()), name='scene_list')
]

