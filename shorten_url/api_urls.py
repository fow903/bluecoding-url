
from django.urls import path
from . import views

urlpatterns = [
    path('shorten_url/', views.shorten_url, name='shorten_url'),
    path('top_visited_urls/', views.get_top_visited_urls, name='top_visited_urls')
]