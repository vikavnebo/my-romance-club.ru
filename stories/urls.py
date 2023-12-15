from django.urls import path
from .views import *

urlpatterns = [
    path('', StoryView.as_view(), name='stories'),
]
