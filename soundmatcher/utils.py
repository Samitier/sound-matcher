


# String to int, returns 0 if string can't be parsed.
def int_or_default(string):
	try:
		return int(string)
	except ValueError:
		return 0
