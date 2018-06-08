
def int_or_default(string):
	try:
		return int(string)
	except ValueError:
		return 0