from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render

from .models import Search, Match
from django.shortcuts import redirect


def index(request):
	return redirect('/static/index.html', permanent=True)

def searches(request):
	return _jsonResponse(Search.objects.all())


def matches(request, search_id):
	return _jsonResponse(Match.objects.filter(search=search_id).order_by('score'))


def _jsonResponse(collection):
	serializedData = serializers.serialize('json', collection)
	return HttpResponse(serializedData, content_type='application/json')
