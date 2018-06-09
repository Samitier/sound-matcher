from django.urls import path
from . import views

urlpatterns = [
	path('api/searches', views.searches, name='searches'),
	path('api/matches/<int:search_id>', views.matches, name='matches'),
	path('', views.index, name='index')
]
