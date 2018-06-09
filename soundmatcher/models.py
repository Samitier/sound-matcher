from django.db import models



# Base abstract class for the recording info
class RecordingInfo(models.Model):
	artist = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	isrc = models.CharField(max_length=200)
	duration = models.IntegerField()

	def __str__(self):
		return self.artist + ' - ' + self.title

	class Meta:
		abstract = True


class Recording(RecordingInfo):
	pass


class Search(RecordingInfo):
	pass


class Match(models.Model):
	recording = models.ForeignKey(Recording, on_delete=models.CASCADE)
	search = models.ForeignKey(Search, on_delete=models.CASCADE)
	score = models.IntegerField(default=9999)
