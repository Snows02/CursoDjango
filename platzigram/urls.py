"""platzigram URL Configuration
"""

from django.urls import path

from platzigram import views as local_views
from posts import views as posts_views

'''
El primer parametro que recibe path es la url a la que esperasmos responder
y el segundo es el nombre de la vista
'''
urlpatterns = [
    path('hello-world/', local_views.hello_world),
    path('sorted/', local_views.sorted_by_get),
    path('hi/<str:name>/<int:age>/', local_views.say_hi),

    path('posts', posts_views.list_posts),
]