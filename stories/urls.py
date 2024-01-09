from django.urls import path
from .views import *

urlpatterns = [
    path('', StoryView.as_view(), name='story_list'),
    path('<slug:story>/', CharacterView.as_view(), name='character_list'),
    path('<slug:story>/<slug:character>/', SceneView.as_view(), name='scene_list')
]

