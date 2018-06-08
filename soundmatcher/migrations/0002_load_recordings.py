# Generated by Django 2.0.6 on 2018-06-08 17:23

from django.db import migrations
import csv
import os

from soundmatcher.models import Recording
from soundmatcher.utils import int_or_default

csv_path = os.path.join(os.path.dirname(__file__), '../raw_data/sound_recordings.csv')

def load_recordings(apps, schema_editor):
	with open(csv_path) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			Recording(
				artist = row['artist'],
				title = row['title'],
				isrc = row['isrc'],
				duration = int_or_default(row['duration'])
			).save()

def delete_recordings(apps, schema_editor):
	Recording.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('soundmatcher', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_recordings, delete_recordings),
    ]
