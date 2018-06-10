from soundmatcher.models import Recording, Search

min_steps = 0
max_recording_duration_steps = 20

# At a greater score than score_threshold, the search and the sound will be declared 100% different
steps_threshold = 20

# Returns the percentage of confidence in which the algorithm thinks two sounds are the same or not.
def get_similarity_percent(search: Search, recording: Recording):
	steps = get_similarity_steps(search, recording)
	return (abs(steps_threshold - min(steps, steps_threshold)) / steps_threshold) * 100

# Similarity steps between a search and a recording are the mean of the number of
# changes needed to reach the recording for every property of search.
# IE: it will return 0 if search is completely equal to recording
#	n if search and the recording differ by n character changes in every prop, etc
def get_similarity_steps(search: Search, recording: Recording):
	steps = []
	# Since IRSC is a unique identifier, if a search has the same isrc of a recording, then the
	# similarity will be the maximum possible. If not, the levenshtein algorithm will be used, in
	# case there's a typo in the search's isrc.
	if search.isrc != '' and recording.isrc != '':
		if search.isrc == recording.isrc:
			return min_steps
		else:
			steps.append(_levenshtein(search.isrc, recording.isrc))
	# For every other field, if the values exist in both search and recording, we will use the levenshtein
	# algorithm to calculate the number of steps needed to reach equality.
	if search.artist != '' and recording.artist != '':
		steps.append(_levenshtein(search.artist, recording.artist))
	if search.title != '' and recording.title != '':
		steps.append(_levenshtein(search.title, recording.title))
	# Since the duration is an integer, the similarity will be based on how close are both values
	# of each other. We give it a max value to not break the rest of the ponderations when calculating
	# the mean.
	if search.duration > 0 and recording.duration > 0:
		duration_steps = abs(search.duration - recording.duration)
		steps.append(min(duration_steps, max_recording_duration_steps))
	# If there are no steps, that means that the search or the recording was empty and it should return
	# maximum inequality.
	if len(steps) == 0:
		return steps_threshold
	# Else we return the mean of all the steps needed to reach the recording values for each prop.
	return sum(steps[0:len(steps)]) / len(steps)



# Implementation of the levenshtein distance algorithm:
# 	https://en.wikipedia.org/wiki/levenshtein_distance
#	https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/levenshtein_distance#Python
# Given two strings s, t, the algorithm returns the number of letter edits needed to change one
# into the other.
def _levenshtein(s, t):
	if s == t:
		return 0
	elif len(s) == 0:
		return len(t)
	elif len(t) == 0:
		return len(s)
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
