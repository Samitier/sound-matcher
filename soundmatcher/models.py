from django.db import models

# Same attributes in Recording and search. 
# Maybe inheritance would be better than repeating the model.

class Recording(models.Model):
	artist = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	isrc = models.CharField(max_length=200)
	duration = models.IntegerField()

class Search(models.Model):
	artist = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	isrc = models.CharField(max_length=200)
	duration = models.IntegerField()

	recording = models.ForeignKey(Recording, on_delete=models.CASCADE)
	score = models.IntegerField(default=0)
