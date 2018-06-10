from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework.renderers import JSONRenderer

from .models import Search, Match
from .serializers import SearchSerializer, MatchSerializer


def index(request):
	return redirect('/static/index.html', permanent=True)

def searches(request):
	serializer = SearchSerializer(Search.objects.all().order_by('title'), many=True)
	return _jsonResponse(serializer)


def matches(request, search_id):
	matches = Match.objects.filter(search=search_id).order_by('-score')
	serializer = MatchSerializer(matches, many=True)
	return _jsonResponse(serializer)


def _jsonResponse(serializer):
	data = JSONRenderer().render(serializer.data)
	return HttpResponse(data, content_type='application/json')
