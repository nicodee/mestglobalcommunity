from google.appengine.ext import db
from google.appengine.ext.blobstore import blobstore
import string
import random
import access
import hashlib
import time
import datetime
import exceptions

class User(db.Model):
    confirmation_status = db.StringProperty()
    first_name          = db.StringProperty()
    last_name           = db.StringProperty()
    email               = db.StringProperty()
    alias               = db.StringProperty()
    picture             = db.StringProperty()
    industry	        = db.StringProperty()
    location	        = db.StringProperty()
    user_id		        = db.StringProperty()
    linkedin_profile    = db.StringProperty()
    notify_mail         = db.StringProperty()
    summary             = db.TextProperty()
    user_profile        = db.StringProperty(choices=set(['Administrator','Mentor','Entrepreneur','Job Applicant']))  
    created             = db.DateTimeProperty(auto_now_add=True)
    declined            = db.DateTimeProperty()
    confirmed           = db.DateTimeProperty()

    @classmethod
    def create(cls,user_data,user_profile):
        email_address = user_data.get('emailAddress')
        results  = cls.gql("WHERE email=:1",email_address)
        count    = results.count()
        alias    = access.createAlias( user_data.get('firstName') + " " + user_data.get('lastName') ) + "@mestmentorplatform.appspotmail.com"

        if count==0:
            user = User(
                        first_name       = user_data.get('firstName'),
                        last_name        = user_data.get('lastName'),
                        email            = user_data.get('emailAddress'),
                        picture          = user_data.get('big_pic'),
                        industry         = user_data.get('industry'),
                        location         = user_data.get('location') and user_data.get('location').get('name'),
                        user_id          = user_data.get('id'),
                        summary          = user_data.get('summary'),
                        notify_mail      = user_data.get('emailAddress'),
                        linkedin_profile = user_data.get('publicProfileUrl'),
                        user_profile     = user_profile,  
                        alias            = alias,
                        confirmation_status  = access.confirmation_status()  
            )    
            return user
        else:
            return 'User already exists'  

    @classmethod
    def delete(cls,user):   
        result = cls.gql("WHERE user_id=:1 and email=:2",user.user_id, user.email)
        if result.count() == 0:
            return True
        else: 
            db.delete(result)

    @classmethod
    def status(cls,user):
        result = cls.gql("WHERE user_id=:1 and email=:2",user.user_id, user.email)
        if result.count() == 0:
            return True
        elif result.count()==1:
            user = result.get()
            user.confirmation_status = "confirmed"
            user.put()
            return True
        else: 
            return False

    @classmethod
    def confirm(cls,new_user_id):
        new_user = User.get_by_id(int(new_user_id))
        new_user.confirmation_status = "confirmed"
        new_user.confirmed  = datetime.datetime.now()
        new_user.put()
        return "confirmed"

    @classmethod
    def decline(cls, user_id):
        declined_user = User.get_by_id(int(user_id))
        declined_user.confirmation_status = "declined"
        declined_user.declined  = datetime.datetime.now()
        declined_user.put()
        return "declined"

class Education(db.Model):
    user            = db.ReferenceProperty(User, collection_name = "educations")
    school_name     = db.StringProperty()
    field_of_study  = db.StringProperty()
    start_date      = db.StringProperty()
    end_date        = db.StringProperty()
    activities      = db.TextProperty()
    notes 	        = db.TextProperty()
    created         = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def create(cls, user, education):
        new_education = Education(
            user            = user,
            school_name     = education.get('schoolName'),
            field_of_study  = education.get('fieldOfStudy'),
            start_date      = str(education.get('startDate').get('year')),
            end_date        = str(education.get('endDate').get('year')),
            activities      = education.get('activities'),
            notes           = education.get('notes')
        )

        new_education.put()

    @classmethod
    def delete(cls,user):   
        result = cls.gql("WHERE user=:1",user)
        if result.count() == 0:
            return True
        else: 
            db.delete(result)

class Position(db.Model):
    user        = db.ReferenceProperty(User, collection_name = "positions")
    position_id = db.StringProperty()
    title       = db.StringProperty()
    summary     = db.TextProperty()
    start_date  = db.StringProperty()
    end_date    = db.StringProperty()
    is_current  = db.BooleanProperty()
    company     = db.StringProperty()
    created     = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def create(cls, user, position):

        new_position = Position(
            user        = user,
            position_id = str(position.get('id')),
            title       = position.get('title'),
            summary     = position.get('summary'),
            start_date  = str(position.get('startDate')['year']),
            end_date    = position.get('endDate') and str(position.get('endDate')['year']),
            is_current  = position.get('isCurrent'),
            company     = position.get('company')['name']
        )

        new_position.put()

    @classmethod
    def delete(cls,user):   
        result = cls.gql("WHERE user=:1",user)
        if result.count() == 0:
            return True
        else: 
            db.delete(result)

class Skills(db.Model):
    user     = db.ReferenceProperty(User, collection_name = "skills")
    name     = db.StringProperty()
    created  = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def create(cls,user,skill):

        skills = Skills(
            user = user,
            name = skill.get('skill').get('name')
        )
        
        skills.put()        

    @classmethod
    def delete(cls,user):   
        result = cls.gql("WHERE user=:1",user)
        if result.count() == 0:
            return True
        else: 
            db.delete(result)

class Entrepreneur(db.Model):
    user        = db.ReferenceProperty(User, collection_name = 'entrepreneurprofile')
    company_name = db.StringProperty()
    designation = db.StringProperty()
    website     = db.StringProperty()
    created     = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def create(cls,user,company_name,designation,website):
        entrepreneur = Entrepreneur(
            user         = user,
            company_name = company_name,
            designation  = designation,
            website      = website
        )
        entrepreneur.put()
        user.confirmation_status = "confirmed"
        user.put()
        return True

    @classmethod
    def delete(cls,user):   
        result = cls.gql("WHERE user=:1",user)
        if result.count() == 0:
            return True
        else: 
            db.delete(result)

class Program(db.Model):
    user               = db.ReferenceProperty(User, collection_name = 'programs')
    program_type       = db.StringProperty(required=True, choices=set(['MEST Strike Force', 'MBA Consultant', 'Senior Advisor', 'Expert in Residence', 'Job Applicant']))
    preferred_email    = db.StringProperty()
    mini_bio           = db.TextProperty() 
    time_zone          = db.StringProperty()
    hours              = db.IntegerProperty()
    created            = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def create(cls,user,program_data):
        results  = cls.gql("WHERE user=:1",user)
        count    = results.count()

        if count==0 and user.user_profile=="Mentor":
            program = Program(
                user                  = user,
                program_type          = program_data.get('program_type'),
                commitment_level      = program_data.get('commitment_level'),
                preferred_email       = program_data.get('email'),
                mini_bio              = program_data.get('mini_bio'),
                time_zone             = program_data.get('time_zone'),
                hours                 = program_data.get('hours')              
            )    
            return program
        elif count==0 and user.user_profile=="Job Applicant":
            program = Program(
                user                  = user,
                program_type          = "Job Applicant",
                mini_bio              = program_data.get('mini_bio'), 
                preferred_email       = program_data.get('email')              
            )    
            return program
        else:
            return False

    @classmethod
    def delete(cls,user):   
        result = cls.gql("WHERE user=:1",user)
        if result.count() == 0:
            return True
        else: 
            db.delete(result)

class Contribution(db.Model):    
    program     = db.ReferenceProperty(Program, collection_name='contributions')
    company     = db.StringProperty()
    contributed_hours   = db.IntegerProperty()
    description  = db.TextProperty()
    created = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def add_contribution(cls, contribution):
        result = cls.gql("WHERE program=:1 and company=:2 and contributed_hours=:3 and description=:4",
                            contribution.get("program", ""), 
                            contribution.get("company", ""),
                            contribution.get("hours", ""),
                            contribution.get("description", "")
                        )

        if result.count() == 0:
            new_contribution = Contribution(
                program = contribution.get("program"),
                company = contribution.get("company"),
                contributed_hours = int(contribution.get("hours")),
                description = contribution.get("description")
                )
            new_contribution.put()
            return True
        else:
            return True




class Resource(db.Model):
    user         = db.ReferenceProperty(User, collection_name='resources')
    resource_key = blobstore.BlobReferenceProperty()
    title        = db.TextProperty()
    description  = db.TextProperty()
    rating       = db.IntegerProperty()
    created      = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def industry(cls, industries, resource):
        for industry in industries:
            Sector.createResource(resource, industry)

    @classmethod
    def expertise(cls, experts, resource):
        for expertise in experts:
            Topic.createResource(resource, expertise)

    @classmethod
    def create(cls,user_id,resource_key, title, description, industry, expertise):
        user = User.get_by_id(int(user_id))
        new_resource = Resource(
                        user         = user,
                        resource_key = resource_key,
                        title        = title,
                        description  = description
                        )
        new_resource.put() 
        cls.expertise(expertise, new_resource)
        cls.industry(industry, new_resource)
        return new_resource 

    @classmethod
    def delete(cls,user,resource_key):   
        result = cls.gql("WHERE user=:1 and resource_key",user,resource_key)
        if result.count() == 0:
            return True
        else: 
            db.delete(result)


class Topic(db.Model):
    program     = db.ReferenceProperty(Program, collection_name='topics')
    resource    = db.ReferenceProperty(Resource, collection_name="topic")
    criteria    = db.StringProperty()
    value       = db.StringProperty()
    created     = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def create(cls,program,topic):
        results  = cls.gql("WHERE program=:1 and criteria=:2 and value=:3",program, topic.get('criteria'), topic.get('value'))
        count    = results.count()

        if count==0:
            new_topic = Topic(
                program    = program,
                criteria   = topic.get('criteria'),
                value      = topic.get('value')              
            )    
            new_topic.put() 

    @classmethod
    def createResource(cls, resource, topic):       
        results  = cls.gql("WHERE resource=:1 and criteria=:2 and value=:3", resource, topic.get('criteria'), topic.get('value')) 
        count    = results.count()

        if count==0:
            new_topic = Topic(
                resource   = resource,
                criteria   = topic.get('criteria'),
                value      = topic.get('value')              
            )    
            new_topic.put()

    @classmethod
    def delete(cls,program):   
        result = cls.gql("WHERE program=:1",program)
        if result.count() == 0:
            return True
        else: 
            db.delete(result)

    @classmethod
    def remove_mentor_topic(cls, value, criteria, program):
        result = cls.gql('WHERE program=:1 and value=:2 and criteria=:3', program, value, criteria)
        count = result.count()

        if count > 0:
            db.delete(result)
            return True
        else: 
            return True

class Sector(db.Model):
    program   = db.ReferenceProperty(Program, collection_name='sectors')   
    resource  = db.ReferenceProperty(Resource, collection_name="sector")
    value     = db.StringProperty()
    created   = db.DateTimeProperty(auto_now_add=True)
 
    @classmethod
    def create(cls,program,sector):
        results  = cls.gql("WHERE program=:1 and value=:2",program, sector.get('value'))
        count    = results.count()

        if count==0:
            new_sector    = Sector(
                program   = program,
                value     = sector.get('value')              
            )    
            new_sector.put() 

    @classmethod
    def createResource(cls, resource, sector):
        results  = cls.gql("WHERE resource=:1 and value=:2",resource, sector.get('value'))
        count    = results.count()

        if count==0:
            new_sector    = Sector(
                resource  = resource,
                value     = sector.get('value')              
            )    
            new_sector.put() 

    @classmethod
    def delete(cls,program):   
        result = cls.gql("WHERE program=:1",program)
        if result.count() == 0:
            return True
        else: 
            db.delete(result)

    @classmethod
    def remove_mentor_sector(cls, value, program):
        result = cls.gql('WHERE program=:1 and value=:2', program, value)
        count = result.count()

        if count > 0:
            db.delete(result)
            return True
        else: 
            return True

class Discovery(db.Model):
    program  = db.ReferenceProperty(Program, collection_name='discovery')
    method   = db.StringProperty()
    value    = db.StringProperty()
    created  = db.DateTimeProperty(auto_now_add=True) 

    @classmethod
    def create(cls,program,discovery):
        results  = cls.gql("WHERE program=:1 and method=:2",program, discovery.get("method"))
        count    = results.count()

        if count==0:    
            new_discovery  = Discovery(
                program    = program,
                method     = discovery.get("method"),
                value      = discovery.get("value")              
            )    
            new_discovery.put() 

    @classmethod
    def delete(cls,program):   
        result = cls.gql("WHERE program=:1",program)
        if result.count() == 0:
            return True
        else: 
            db.delete(result)


class Message(db.Model):
    msg_id           = db.StringProperty()
    msg_type         = db.StringProperty()
    sender           = db.ReferenceProperty(User, collection_name='sent')
    receiver         = db.ReferenceProperty(User, collection_name='received')
    receiver_email   = db.StringProperty()
    sender_email     = db.StringProperty()
    subject          = db.StringProperty()
    starred          = db.StringProperty()
    category         = db.StringProperty()
    content          = db.TextProperty()
    status           = db.StringProperty(choices=set(['read','unread','trash']))
    date_sent        = db.StringProperty()
    created          = db.DateTimeProperty(auto_now_add=True)
    deleted          = db.DateTimeProperty(auto_now_add=False)
    sender_deleted   = db.StringProperty()
    receiver_deleted = db.StringProperty()

    @classmethod
    def state_generator(cls,size=50, chars=string.ascii_uppercase + string.digits):
        msg_id = "".join(random.choice(chars) for x in range(size))
        results  =  cls.gql("WHERE msg_id=:1",msg_id)
        if results.count() == 0:
            return msg_id
        else:
            state_generator()

    @classmethod
    def create(cls,message):
        if message:
            msg = Message(
                            msg_id           = Message.state_generator(),
                            sender           = message.get('sender'),
                            sender_email     = message.get('sender_email'),
                            receiver_email   = message.get('receiver_email'),
                            receiver         = message.get('receiver'),             
                            subject          = message.get('subject'),
                            category         = message.get('category'),
                            content          = message.get('content'),
                            date_sent        = message.get('date'),
                            msg_type         = message.get('type'),
                            status           = "unread",
                            starred          = "False",
                            sender_deleted   = "False",
                            receiver_deleted = "False"
                        )
            msg.put()
            return True
        else:
            return False

    @classmethod
    def getMessage(cls,msg_id, read_status):
        msg = Message.get_by_id(int(msg_id))
        msg.status = read_status
        msg.put()
        return msg

    @classmethod
    def displayMessage(cls,msg_id):
        msg = Message.get_by_id(int(msg_id))
        msg.status = "read"
        msg.put()
        return msg

    @classmethod
    def change_status(cls,msg_id,status):
        print msg_id
        msg = Message.get_by_id(int(msg_id))
        if msg:
            msg.status = status
            msg.put()
            return True
        else:
            return False

    @classmethod
    def star(cls, msg_id):
        msg = Message.get_by_id(int(msg_id))
        msg.starred = "True"
        msg.put()
        return "starred"

    @classmethod
    def unstar(cls, msg_id):
        msg = Message.get_by_id(int(msg_id))
        msg.starred = "False"
        msg.put()
        return "unstarred"

    @classmethod
    def delete(cls,msg_id):
        result = cls.gql("WHERE msg_id=:1",msg_id)
        if result.count() == 0:
            return True
        else: 
            db.delete(result)
            return True 
        
    @classmethod
    def delete_message(cls, msg_id, user):
        msg = Message.get_by_id(int(msg_id))
        if msg:
            Message.delete_sent(msg, user)
            Message.delete_received(msg, user)
            return True
        else:
            return True
            
    @classmethod
    def delete_sent(cls, msg, user):        
        if msg.sender.email == user.email:
            msg.sender_deleted = "True"
            msg.put()
            return True
        else:
            return True

    @classmethod
    def delete_received(cls, msg, user):
        if msg.receiver.email == user.email:
            msg.receiver_deleted = "True"
            msg.put()
            return True
        else:
            return True

class Favorite(db.Model):
    user          = db.ReferenceProperty(User,  collection_name ="favorites")
    favorite_type = db.StringProperty(required=True, choices=set(['Mentor', 'Job Applicant', 'Resource']))
    favorite_id   = db.StringProperty()
    created       = db.DateTimeProperty(auto_now_add='True')

    @classmethod
    def create(cls, user, favorite_type, favorite_id):
        result = cls.gql("WHERE user=:1 and favorite_type=:2 and favorite_id=:3", user, favorite_type, favorite_id)
        count  = result.count()

        if count == 0:
            new_favorite = Favorite(
                user          = user,
                favorite_type = favorite_type,
                favorite_id   = favorite_id
            )
            new_favorite.put()
            return True

        else:
            return "Already favorited"

    @classmethod
    def check(cls, user, item_id):
        result = cls.gql("WHERE user=:1 and favorite_id=:2", user, item_id).count()
        if result == 0:
            msg = {"favorite":"false", "src":"scripts/img/unlike.png"}
            return msg
        else:
            msg = {"favorite":"true", "src":"scripts/img/like.png"}
            return msg

    @classmethod
    def delete(cls, user, favorite_type, favorite_id):
        result = cls.gql("WHERE user=:1 and favorite_type=:2 and favorite_id=:3", user, favorite_type, favorite_id)
        if result.count() == 0:
            return True
        else: 
            db.delete(result)
            return True 


class Rating(db.Model):
    user          = db.ReferenceProperty(User,  collection_name ="rating")
    rating_type   = db.StringProperty(required=True, choices=set(['Mentor', 'Job Applicant', 'Resource']))
    rating_id     = db.StringProperty()
    rating_value  = db.StringProperty()
    created       = db.DateTimeProperty(auto_now_add='True')

    @classmethod
    def rate(cls, user, rating_type, rating_id,rating_value):
        result = cls.gql("WHERE user=:1 and rating_type=:2 and rating_id=:3", user, rating_type, rating_id)
        count  = result.count()

        if count == 0:
            new_rating = Rating(
                user          = user,
                rating_type   = rating_type,
                rating_id     = rating_id,
                rating_value  = rating_value
            )
            new_rating.put()
            return True

        else:
            rating = result.get()
            rating.rating_value = rating_value
            rating.put()
            return True

    @classmethod
    def check(cls, user, item_id):
        result = cls.gql("WHERE user=:1 and rating_id=:2", user, item_id)
        count = result.count()
        if count == 0:
            value = 0
            msg   = {"rated":"false", "value":value}
            return msg
        else:
            rating = result.get()
            value  = rating.rating_value
            msg    = {"rated":"true", "value":float(value)}
            return msg


class Comment(db.Model):
    user           = db.ReferenceProperty(User, collection_name="comments_received") 
    resource       = db.ReferenceProperty(Resource, collection_name='comments_received')
    entity_id      = db.StringProperty()
    commentor      = db.ReferenceProperty(User, collection_name="comments_made")
    commentor_name = db.StringProperty()
    commentor_id   = db.StringProperty()
    content        = db.TextProperty()
    created        = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def create(cls, comment):
        if (comment.get('type')) == "resource" and (Comment.check(comment) == 0):
        # if (comment.get('type')) == "resource":
            comment = Comment(
                            resource       = comment.get('entity'),
                            entity_id      = comment.get('entity_id'),
                            commentor      = comment.get('commentor'),
                            commentor_name = comment.get('commentor').first_name + " " + comment.get('commentor').last_name,
                            commentor_id   = comment.get('commentor_id'),
                            content        = comment.get('content')
                            )
            comment.put()
            return {"status": True, "value": comment.key().id()}

        elif (comment.get('type')) == "user" and (Comment.check(comment) == 0):
        # elif (comment.get('type')) == "user":
            print "hello========================"
            comment = Comment(
                            user           = comment.get('entity'),
                            entity_id      = comment.get('entity_id'),
                            commentor      = comment.get('commentor'),
                            commentor_name = comment.get('commentor').first_name + " " + comment.get('commentor').last_name,
                            commentor_id   = comment.get('commentor_id'),
                            content        = comment.get('content')
                            )            
            comment.put()
            print comment.key().id()
            return {"status": True, "value": comment.key().id()}

        else:
            return {"status": False, "value": None}

    @classmethod
    def edit(cls, comment):
        comment_id = comment.get("comment_id")
        try:
            editable_comment = Comment.get_by_id(int(comment_id)) 
            editable_comment.content = comment.get("content")
            editable_comment.put()
            return {"status": True, "value": editable_comment.content}
        except:
            return {"status": False, "value": None}

    @classmethod
    def delete(cls, comment): 
        comment_id = comment.get("comment_id")
        print "=============================="
        print comment_id
        print "=============================="
        try:
            item_to_delete = Comment.get_by_id(int(comment_id))
            db.delete(item_to_delete)
            return {"status": True, "value": None}
        except:
            print "yeah"
            return {"status": False, "value": None}

    @classmethod
    def check(cls, comment):
        print "=============================="
        print comment
        print "=============================="
        result = cls.gql("WHERE entity_id=:1 and commentor_id=:2", comment.get('entity_id'), comment.get('commentor_id'))
        print result.count()
        if result.count() > 0:
            # count = 0
            # for item in result:
            #     if comment.get('content') == item.content:
            #         count +=1
            return result.count()
        else:
            return 0
        
class Administrator(db.Model):
    user          = db.ReferenceProperty(User, collection_name =  "administrator")
    username      = db.StringProperty()
    password_hash = db.StringProperty()
    salt          = db.StringProperty() 
    created       = db.DateTimeProperty(auto_now_add = True)

    @staticmethod
    def make_salt():
        return ''.join(random.choice(string.letters) for i in range(5))
    
    @classmethod
    def make_pw_hash(cls,pw,salt):
        pw_hash = pw+salt
        return hashlib.sha256(pw_hash).hexdigest()

    @classmethod
    def create(cls, user, password, username):
        result = cls.gql("WHERE user=:1", user)
        count  = result.count()

        if count==0:
            salt = ''
            salt = Administrator.make_salt()
            password_hash = cls.make_pw_hash(password, salt)
            admin = Administrator(user = user, password_hash = password_hash, username = username, salt = salt)
            admin.put()
            return True
        else:
            return False

    @classmethod
    def change_password(cls, user, old_password, new_password):
        admin = cls.gql("WHERE user=:1", user).get()
        count  = result.count()

        if admin:
            password_hash = cls.make_pw_hash(old_password, admin.salt)
            if password_hash == admin.password:
                admin.password = new_password
                admin.put()
                return True      
        else:
            return False

    @classmethod
    def log_in_admin(cls,username,password):
        # user = User.all().filter("email =", email).get()
        results = Administrator.all().filter("username =", username).get()

        if results:
            password_hash = cls.make_pw_hash(password, results.salt)
            if password_hash == results.password_hash:
                return results.key().id()
        else:
            return False

    @classmethod
    def delete_admin(cls, user):
        result = cls.gql("WHERE user=:1", user)
        count  = result.count()

        if count == 1:
            admin_to_be_deleted = result.get()
            admin_to_be_deleted.delete()
            return True
        else: 
            return False


class Jobs(db.Model):
    user             = db.ReferenceProperty(User, collection_name="jobs")
    job_unique_id    = db.StringProperty()
    job_title        = db.StringProperty() 
    hiring_company   = db.StringProperty()
    job_description  = db.TextProperty()
    job_status       = db.StringProperty(required =True, choices=set(['Available', 'Removed']))
    job_requirements = db.StringProperty()
    job_url          = db.StringProperty()
    deadline         = db.StringProperty()
    created          = db.DateTimeProperty(auto_now_add=True)
    removed_on       = db.DateTimeProperty()

    @classmethod
    def state_generator(cls,size=50, chars=string.ascii_uppercase + string.digits):
        job_unique_id = "".join(random.choice(chars) for x in range(size))
        results  =  cls.gql("WHERE resource_id=:1",job_unique_id)
        if results.count() == 0:
            return job_unique_id
        else:
            state_generator() 

    @classmethod
    def create(cls, user_id, job):
        new_job = Jobs(user=User.get_by_id(int(user_id)),
                       job_unique_id=Jobs.state_generator(),
                       job_title=job.get("title"),
                       hiring_company=job.get("company"),
                       job_requirements = job.get("requirements"),
                       job_description=job.get("description"),
                       job_status=job.get("status"),
                       job_url=job.get("url"),
                       deadline=job.get("deadline"),
                       )
        new_job.put()
        return True

    @classmethod
    def edit(cls, user, job):
        try:
            edited_job = Jobs.get_by_id(int(job.get("job_id")))
            edited_job.job_title = job.get("job_title")
            edited_job.hiring_company = job.get("hiring_company")
            edited_job.job_description = job.get("description")
            edited_job.deadline        = job.get("deadline")
            edited_job.job_requirements = job.get("requirements")
            edited_job.put()

            return {"action":"edit","status":True, "job_id": job.get("job_id")}

        except:
            return {"action":"edit","status":False}

    @classmethod
    def delete(cls, job_id, user):
        job = Jobs.get_by_id(int(job_id))
        if user.user_profile == "Administrator" or job.user == user:
            job.job_status = "Removed"
            job.removed_on = datetime.datetime.now()
            job.put()
            return {"action":"delete", "status":True}
        else:            
            return {"action":"delete", "status":False}


class Subscriber(db.Model):
    subscriber_name  = db.StringProperty()
    subscriber_email = db.StringProperty()
    created          = db.DateTimeProperty(auto_now_add=True)
    unsubscribed     = db.DateTimeProperty()
    status           = db.StringProperty()

    @classmethod
    def subscribe(cls, email, name):
        result = Subscriber.all().filter("subscriber_email =", email).count()

        if result == 0:
            new_subscriber = Subscriber(
                                        subscriber_name = name,
                                        subscriber_email= email,
                                        status          = "subscribed"
                                        )
            new_subscriber.put()
            value = True

        else:
            value = False            
        
        return {"action":"subscribe", "status":value}
    
    @classmethod
    def unsubscribe(cls, email):
        result = cls.gql("WHERE subscriber_email=:1 and status=:2", email, "subscribed")

        if result.count() > 0:
            unsubscriber = result.get()
            unsubscriber.status = "unsubscribed"
            unsubscriber.unsubscribed = datetime.datetime.now()
            unsubscriber.put()
            value = True
        else:
            value = False

        return {"action":"unsubscribe", "status":value}


    @classmethod
    def delete(cls, email):        
        result = cls.gql("WHERE subscriber_email=:1", email)

        if result.count() > 0:
            deleted_subscriber = result.get()
            db.delete(deleted_subscriber)
            value = True
        else:
            value = False

        return {"action":"delete", "status":value}


