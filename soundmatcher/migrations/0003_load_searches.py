# Generated by Django 2.0.6 on 2018-06-08 18:10

from django.db import migrations
import csv
import os

from soundmatcher.models import Recording, Search
from soundmatcher.utils import int_or_default, calc_similarity

csv_path = os.path.join(os.path.dirname(__file__), '../raw_data/sound_recordings_input_report.csv')

def load_searches(apps, schema_editor):
	with open(csv_path) as csvfile:
		reader = csv.DictReader(csvfile)
		recordings = Recording.objects.all()
		for row in reader:
			search = Search(
				artist = row['artist'],
				title = row['title'],
				isrc = row['isrc'],
				duration = int_or_default(row['duration']),
			)
			search.score = 9999
			search.recording = recordings.first()
			for recording in recordings:
				score = calc_similarity(search, recording)
				if score < search.score:
					search.score = score
					search.recording = recording

			search.save()

def delete_searches(apps, schema_editor):
	Search.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('soundmatcher', '0002_load_recordings'),
    ]

    operations = [
        migrations.RunPython(load_searches, delete_searches),
    ]
