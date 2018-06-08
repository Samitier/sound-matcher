from soundmatcher.models import Recording, Search

# String to int, returns 0 if string can't be parsed.
def int_or_default(string):
	try:
		return int(string)
	except ValueError:
		return 0

# Similarity between a search and a recording will be given as the mean of the number of changes needed
# to reach the recording for every property of search.
# IE: it will return 0 if search is completely equal to recording
#	1 if search and the recording differ only by one character change, etc
def calc_similarity(search: Search, recording: Recording):
	steps = []
	# Since IRSC is a unique identifier, if a search has the same isrc of a recording, then the
	# similarity will be the maximum possible. If not, the levenshtein algorithm will be used, in
	# case there's a typo in the search's isrc.
	if search.isrc != '' and recording.isrc != '': 
		if search.isrc == recording.isrc:
			return 0
		else:
			steps.append(levenshtein(search.isrc, recording.isrc))
	# For every other field, if the values exist in both search and recording, we will use the levenshtein
	# algorithm to calculate the number of steps needed to reach equality.
	if search.artist != '' and recording.artist != '':
		steps.append(levenshtein(search.artist, recording.artist))
	if search.title != '' and recording.title != '':
		steps.append(levenshtein(search.title, recording.title))
	# Since the duration is an integer, the similarity will be based on how close are both values
	# of each other.
	if search.duration > 0 and recording.duration > 0:
		steps.append(abs(search.duration - recording.duration))
	# If there are no steps, that means that the search or the recording were empty and it should return
	# maximum inequality.
	if len(steps) == 0:
		return 9999
	# Else we return the mean of all the steps needed to reach the recording values for each prop.
	return sum(steps[0:len(steps)]) / len(steps)

# Implementation of the levenshtein distance algorithm: 
# 	https://en.wikipedia.org/wiki/Levenshtein_distance
#	https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python
# Given two strings s, t, the algorithm returns the number of letter edits needed to change one 
# into the other.
def levenshtein(s, t):
	if s == t: return 0
	elif len(s) == 0: return len(t)
	elif len(t) == 0: return len(s)
	v0 = [None] * (len(t) + 1)
	v1 = [None] * (len(t) + 1)
	for i in range(len(v0)):
		v0[i] = i
	for i in range(len(s)):
		v1[0] = i + 1
		for j in range(len(t)):
			cost = 0 if s[i] == t[j] else 1
			v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
		for j in range(len(v0)):
			v0[j] = v1[j]

	return v1[len(t)]