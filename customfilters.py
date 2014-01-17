from models import Rating, User, Comment

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

def hours_committed(mentor):
	total = 0
	if mentor.programs[0].contributions.count() > 0 :
		for contribution in mentor.programs[0].contributions:
			total += contribution.contributed_hours

	return total

def hours_left(mentor):
	total = hours_committed(mentor)
	delta = mentor.programs[0].hours - total
	
	if delta > 0:
		return delta
	else:
		return 0

def get_committed_image(mentor, arg):
	image_src= "BadgesSilhouette.png"
	# if hours_committed(mentor) == 0:
	return image_src

def get_rating(mentor_id, arg):
	user = User.get_by_id(int(arg))
	rating = Rating.check(user, str(mentor_id))
	return  rating.get("value")
 
def has_commented(mentor, arg):
	user = User.get_by_id(int(arg))
	result = Comment.check({"entity_id": str(mentor.key().id()), "commentor_id": str(user.key().id())})

	if result > 0:
		return "hide-comment-box"
	else:
		return "show-comment-box"
	print "======================="
	print result
	print "======================="
	# return result