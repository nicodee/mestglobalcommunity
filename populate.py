from google.appengine.ext import db
from models import *

def authenticate(user_data):
	email_address = user_data.get('emailAddress')
	user_id      = user_data.get('id')
	user         = User.gql("Where email=:1 and user_id=:2",email_address,user_id).get()
	
	if user:
		return user
	else:
		return "User does not exist"

def create_user(user_data,user_profile):
	user = User.create(user_data,user_profile)

	if user == 'User already exists':
		return user

	else:
		user.put()

		def education_detail():
			if read(user_data,'educations') > 0:
				for school in user_data.get('educations')['values']:
					Education.create(user, school)
			else:
				pass

		def position_detail():
			if read(user_data,'positions') > 0:
				for position in user_data.get('positions')['values']:
					Position.create(user, position)
			else:
				pass		

		def skill_detail():
			if read(user_data,"skills") > 0:
				for skill in user_data.get('skills')['values']:
					Skills.create(user,skill)
			else:
				pass				

		education_detail()
		position_detail()
		skill_detail()

	return user

def create_program(user,program_data):
	program = Program.create(user,program_data)

	if program:
		program.put()

		def topic_detail():
			if read_program(program_data, 'topic') > 0:
				for topic in program_data.get('topic'):
					Topic.create(program, topic)

		def sector_detail():
			if read_program(program_data, 'sector') > 0:
				for sector in program_data.get('sector'):
					Sector.create(program,sector)	

		def discovery_detail():
			if read_program(program_data, 'referral') > 0:
				for discovery in program_data.get('referral'):
					Discovery.create(program,discovery)		

		topic_detail()
		sector_detail()
		discovery_detail()
	
	return program

def delete_user(user):
	def delete_account(user):
		Education.delete(user)
		Position.delete(user)
		Skills.delete(user)
		User.delete(user)

	if user.user_profile == "Mentor":
		result = delete_mentor(user)
	elif user.user_profile == "Admin":
		result = delete_admin(user)
	elif user.user_profile == "Entrepreneur":
		result = delete_entrepreneur(user)	
	elif user.user_profile == "Job Applicant":
		result = delete_job_applicant(user)

	delete_account(user)
	return	True


def delete_mentor(user):
	def delete_program():
		program = Program.gql("WHERE user=:1",user).get()
		Sector.delete(program)
		Topic.delete(program)
		Discovery.delete(program)
		Program.delete(user)
	delete_program()


def delete_job_applicant(user):
	def delete_program():
		program = Program.gql("WHERE user=:1",user).get()
		Sector.delete(program)
		Topic.delete(program)
		Discovery.delete(program)
		Program.delete(user)
	delete_program()


def delete_entrepreneur(user):
	def delete_profile():
		Entrepreneur.delete(user)
	delete_profile()


def read(user_data, category):
	if user_data.get(category):
		return user_data.get(category)["_total"]
	else:
		return 0	


def read_program(program, key):
	if program.get(key):
		return len(program.get(key))
	else:
		return 0


def create_admin():
	deleteKwaku()
	result = User.all().filter("user_profile =", "Administrator").count()
	# pass
	if result < 1:
		new_admin = User(first_name          ="Administrator",
					    last_name           = "",
					    confirmation_status = "confirmed",
					    email               = "nicodemus.nutsukpui@meltwater.org",
					    alias               = "admin@mestmentorplatform.appspotmail.com",
					    picture             = None,
					    industry	        = None,
					    location	        = None,
					    user_id		        = None,
					    linkedin_profile    = None,
					    notify_mail         = "nicodemus.nutsukpui@meltwater.org",
					    summary             = None,
					    user_profile        = 'Administrator'
						)
		new_admin.put()
		setAdmin(new_admin)
	else:
		pass

def setAdmin(new_admin):
	password = "admin" 
	username = "administrator"
	admin    = Administrator.create(new_admin, password, username)

def deleteKwaku():
	result = User.all().filter("email =", "elormm@hotmail.com").count()
	if result > 0:
		kwaku = User.all().filter("email =", "elormm@hotmail.com").get()
		delete_user(kwaku)
	else:
		pass

def edit_profile(value, criteria, perform, user, category):
	program = user.programs[0]
	if category == 'topic':
		if perform == 'delete':
			result = Topic.remove_mentor_topic(value, criteria, program)
			return result
		elif perform =='add':
			Topic.create(program, {'criteria': criteria, 'value': value})
			return True

	elif category =='sector':
		if perform == 'delete':
			result = Sector.remove_mentor_sector(value, program)
			return result
		elif perform =='add':
			Sector.create(program, {'value': value})
			return True
