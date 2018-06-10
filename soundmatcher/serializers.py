from soundmatcher.models import Search, Match
from rest_framework import serializers

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = ('id', 'artist', 'title', 'isrc', 'duration')

class MatchSerializer(serializers.ModelSerializer):
    recording = SearchSerializer()

    class Meta:
        model = Match
        fields = ('score', 'recording')