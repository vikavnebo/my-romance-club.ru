from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from main.views import handler404, handler500

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('stories.urls')),
])
 
handler404 = handler404

handler500 = handler500
