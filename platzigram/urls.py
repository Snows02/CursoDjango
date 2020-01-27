"""platzigram URL Configuration
"""

# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


'''
El primer parametro que recibe path es la url a la que esperasmos responder
y el segundo es el nombre de la vista y el tercero es para poder instaciarlo
en una view y que sea independiente del path que estemos mandando
'''
urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include(('posts.urls', 'posts'), namespace='posts')),
    path('users/', include(('users.urls', 'users'), namespace='users')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
