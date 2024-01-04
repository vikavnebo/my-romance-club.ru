from django.urls import path
from .views import *

urlpatterns = [
    path('', StoryView.as_view(), name='stories'),
    path('<slug:story>/', CharacterView.as_view(), name='story_detail'),
    path('<slug:story>/<slug:url>/', CharacterDetailView.as_view(), name='character_detail')
]

