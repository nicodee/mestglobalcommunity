def is_topic(topics, criteria):
	count = topics.filter('value =', criteria).count()
	if count > 0:
		return 'selected'
	else:
		return ''

def is_sector(sectors, criteria):
	count = sectors.filter('value =', criteria).count()
	if count > 0:
		return 'selected'
	else:
		return ''

def inbox_type(category, arg):
	if category == arg:
		return 'active'