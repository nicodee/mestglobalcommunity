from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from time import gmtime, strftime
from google.appengine.api import mail
from models import *
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import exceptions
import webapp2
import time
import jinja2
import urllib
import json
import string 
import random
import hashlib
import logging
import hmac
import populate
import access
import mailhandler
import m2json
import jsonString
import customfilters
template_dir = "templates"
jinja_env    = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)
#################################custom filters begins#############################################
def true(name):
    return name

def is_topic(topics, criteria):
    return customfilters.is_topic(topics, criteria)

def is_sector(sectors, criteria):
    return customfilters.is_sector(sectors, criteria)

def inbox_type(category, arg):
    return customfilters.inbox_type(category, arg)
#################################custom filters ends#############################################

jinja_env.filters['true'] = true
jinja_env.filters['is_topic'] = is_topic
jinja_env.filters['is_sector'] = is_sector
jinja_env.filters['inbox_type'] = inbox_type

API_Key                   = access.API_Key
Secret_Key                = access.Secret_Key
OAuth_User_Token          = access.OAuth_User_Token
OAuth_User_Secret         = access.OAuth_User_Secret
Redirect_uri_mentor       = access.Redirect_uri_mentor
Redirect_uri_entrepreneur = access.Redirect_uri_entrepreneur
redirect_uri_admin        = access.redirect_uri_admin
Redirect_uri_applicant    = access.Redirect_uri_applicant
Redirect_uri_log_in       = access.Redirect_uri_log_in
Scope_sign_up             = access.Scope_sign_up
Scope_log_in              = access.Scope_log_in
State                     = []
State                     = access.state_generator(State)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)


class RequestHandler(webapp.RequestHandler):
    """
    Parent class for all other webpages.
    """    
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        return render_str(template, **params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))
    def make_secure_val(self, val):
        salt = access.salt
        return "%s|%s" % (val, hmac.new(salt, val).hexdigest())

    def check_secure_val(self, secure_val):
        val = secure_val.split('|')[0]
        if self.make_secure_val(val) == secure_val:
            return val

    def set_secure_cookie(self, name, value, expires=None):
        cookie_val = self.make_secure_val(value)
        if expires:
            self.response.headers.add_header('Set-Cookie', '%s=%s; expires=%s; Path=/' % (name, cookie_val, expires))
        else:
            self.response.headers.add_header('Set-Cookie', '%s=%s; Path=/' % (name, cookie_val))

    def read_secure_cookie(self, name):
        cookie_val = self.request.cookies.get(name)
        if cookie_val and self.check_secure_val(cookie_val):
            return self.check_secure_val(cookie_val)

    def log_user_in(self, user_id): # good
        self.set_secure_cookie('user_id', user_id)

    def log_user_out(self): # good
        self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')

    def initialize(self, *a, **kw): #good
        webapp2.RequestHandler.initialize(self, *a, **kw)
        # begin checks to see if user is logged in
        uid = self.read_secure_cookie('user_id')
        # print uid
        try:
            if uid: #user is logged in with a domain account
                self.user    = User.get_by_id(int(uid))
                self.user_id = uid
                self.user_profile = self.user.user_profile
                self.confirmation_status = self.user.confirmation_status
            else: # user is not logged in
                self.user = None
        except:
            self.log_user_out()
            self.redirect("/home")

class MainPage(RequestHandler):
    def get(self): 
        if self.user: 
            self.redirect('/profilepage')
        else:
            self.redirect('/home') 
   
class ProgramsHandler(RequestHandler):
    def get(self):
        self.render('mentor-programs.html')

    def post(self):
        action = self.request.get('action')
        #when user is a new mentor
        if action == "sign_up_mentor":        
            self.redirect('https://www.linkedin.com/uas/oauth2/authorization?response_type=code&client_id=%s&scope=%s&state=%s&redirect_uri=%s' %(API_Key,Scope_sign_up,State,Redirect_uri_mentor))
       
class HomePageHandler(RequestHandler):
    def get(self):
        self.render('index.html')

    def post(self):
        #determining which action to perform
        action = self.request.get('action')
        
        #when user is a new mentor
        if action == "sign_up_mentor":
            self.redirect('https://www.linkedin.com/uas/oauth2/authorization?response_type=code&client_id=%s&scope=%s&state=%s&redirect_uri=%s' %(API_Key,Scope_sign_up,State,Redirect_uri_mentor))
        
        #when user is an entrepreneur
        elif action == "sign_up_entrepreneur":
            self.redirect('https://www.linkedin.com/uas/oauth2/authorization?response_type=code&client_id=%s&scope=%s&state=%s&redirect_uri=%s' %(API_Key,Scope_sign_up,State,Redirect_uri_entrepreneur))
        
        #when user is a job applicant
        elif action == "sign_up_applicant":
            self.redirect('https://www.linkedin.com/uas/oauth2/authorization?response_type=code&client_id=%s&scope=%s&state=%s&redirect_uri=%s' %(API_Key,Scope_sign_up,State,Redirect_uri_applicant))        
        
        #when user is logging in
        elif action == "login":
            self.redirect('https://www.linkedin.com/uas/oauth2/authorization?response_type=code&client_id=%s&scope=%s&state=%s&redirect_uri=%s' %(API_Key,Scope_log_in,State,Redirect_uri_log_in))
        
        #redirects to home when action doesn't match any of the above
        else:
            self.response.write("/home")

class SignUpEntrepreneur(RequestHandler):
    def get(self):
        self.redirect('https://www.linkedin.com/uas/oauth2/authorization?response_type=code&client_id=%s&scope=%s&state=%s&redirect_uri=%s' %(API_Key,Scope_sign_up,State,Redirect_uri_entrepreneur))
class SignUpMentorHandler(RequestHandler):
    def get(self):
        self.redirect('https://www.linkedin.com/uas/oauth2/authorization?response_type=code&client_id=%s&scope=%s&state=%s&redirect_uri=%s' %(API_Key,Scope_sign_up,State,Redirect_uri_mentor))

class SignInEntrepreneur(RequestHandler):
    def get(self):
        self.redirect('https://www.linkedin.com/uas/oauth2/authorization?response_type=code&client_id=%s&scope=%s&state=%s&redirect_uri=%s' %(API_Key,Scope_log_in,State,Redirect_uri_log_in))

class LogInEntrepreneur(RequestHandler):
    def get(self):
        self.redirect("/signin")

class LogInMentor(RequestHandler):
    def get(self):
        self.redirect("/signin")

#authorizes and fetches mentor details from linkedin redirects to  mentor form.
#further redirects to home when form is successfully filled
#sends alert to admin for confirmation of new mentor
class MentorSignUpPageHandler(RequestHandler): 
    def get(self):
        authorization_code = self.request.get('code')
        state              = self.request.get('state')

        #requesting for accesss token from linkedIn using authorization code
        result             = urllib.urlopen('https://www.linkedin.com/uas/oauth2/accessToken?grant_type=authorization_code&code=%s&redirect_uri=%s&client_id=%s&client_secret=%s' %(authorization_code,Redirect_uri_mentor,API_Key,Secret_Key))

        #checks if action was successful and 'state' is authentic 
        if result.code == 200 and state == State:
            token       = json.loads(result.read())


            #using access token to fetch user data from linkedIn  
            userprofile          = urllib.urlopen('https://api.linkedin.com/v1/people/~:(id,first-name,last-name,location:(name),summary,industry,public-profile-url,positions,recommendations-received,skills:(id,skill),educations:(id,school-name,field-of-study,start-date,end-date,degree,activities,notes),twitter-accounts,picture-url,email-address)?format=json&oauth2_access_token=%s' %(token['access_token']))
            userdata             = json.loads(userprofile.read())
            profilepic           = urllib.urlopen('https://api.linkedin.com/v1/people/~/picture-urls::(original)?format=json&oauth2_access_token=%s' %(token['access_token'])) 
            bigPic               = json.loads(profilepic.read())
            userdata["big_pic"]  = bigPic['values'][0]
            userdata             = jsonString.convert(userdata)
            #rendering form for new mentor to fill
            exists = User.all().filter('email =', userdata['emailAddress']).count()
            if exists > 0 :
                self.render("/duplicate.html")
            else:
                self.render('mentor/mentorsignupform.html', user_data=json.dumps(userdata))            
        #redirects to homepage when action above is not successful     
        else:
            self.redirect('/home')

    def post(self):
        action = self.request.get('action')
        if action == "submit_application":
            # try:
                user_data = json.loads(self.request.get('user_data'))
                user      = populate.create_user(user_data, "Mentor")
                if user=="User already exists":
                    self.log_user_out()
                    message  = json.dumps({"message":"error", "value":user})
                    self.response.write(message)
                else:
                    programUTF  = json.loads(self.request.get('program')) 
                    programJSON = jsonString.convert(programUTF)  
                    program     = populate.create_program(user, programJSON)
                    mail_status = mailhandler.requestMail(user)
                    notifyuser = mailhandler.notificationMail(user)
                    message     = json.dumps({"message":"success", "firstname":user.first_name, "lastname":user.last_name})
                    self.log_user_out()
                    self.response.write(message)

#authorizes and fetches entrepreneur details from linkedin
#further redirects to home when form is successfully filled
#sends alert to admin for confirmation of new entrepreneur
class EntrepreneurSignUpPageHandler(RequestHandler):
    def get(self):
        authorization_code = self.request.get('code')
        state              = self.request.get('state')
        
        try:
            result             = urllib.urlopen('https://www.linkedin.com/uas/oauth2/accessToken?grant_type=authorization_code&code=%s&redirect_uri=%s&client_id=%s&client_secret=%s' %(authorization_code,Redirect_uri_entrepreneur,API_Key,Secret_Key))

            if result.code == 200 and state == State:
                token       = json.loads(result.read())  
                userprofile = urllib.urlopen('https://api.linkedin.com/v1/people/~:(id,first-name,last-name,public-profile-url,location:(name),summary,industry,positions,recommendations-received,skills:(id,skill),educations:(id,school-name,field-of-study,start-date,end-date,degree,activities,notes),twitter-accounts,picture-url,email-address)?format=json&oauth2_access_token=%s' %(token['access_token']))
                userdata    = json.loads(userprofile.read())
                profilepic           = urllib.urlopen('https://api.linkedin.com/v1/people/~/picture-urls::(original)?format=json&oauth2_access_token=%s' %(token['access_token'])) 
                bigPic               = json.loads(profilepic.read())
                userdata["big_pic"]  = bigPic['values'][0]
                user  = populate.create_user(userdata, 'Entrepreneur')
                if user=='User already exists':
                    self.log_user_out()
                    self.render("/duplicate.html")
                else:
                    user_id = user.key().id()
                    self.log_user_in(str(user_id))
                    mail_status = mailhandler.requestMail(user)
                    notifyuser = mailhandler.notificationMail(user)
                    confirmation_msg  = "Your account has been successfully created and is pending approval"
                    self.log_user_out()
                    self.render('/success_entrepreneur.html')
            ########################################### need to send alert to admin for confirmation of new user ####################################################
            else:
                self.redirect("/home")         
        except:
            self.response.write("Something seems to have gone wrong.")


class LoginPageHandler(RequestHandler):
    def get(self):       
        authorization_code = self.request.get('code')
        state              = self.request.get('state')
        result             = urllib.urlopen('https://www.linkedin.com/uas/oauth2/accessToken?grant_type=authorization_code&code=%s&redirect_uri=%s&client_id=%s&client_secret=%s' %(authorization_code,Redirect_uri_log_in,API_Key,Secret_Key))
        
        if result.code == 200 and  state == State :
            token        = json.loads(result.read())   
            userprofile  = urllib.urlopen('https://api.linkedin.com/v1/people/~:(id,first-name,last-name,email-address)?format=json&oauth2_access_token=%s' %(token['access_token']))
            userdata     = json.loads(userprofile.read()) 
            user         = populate.authenticate(userdata)

            if user == "User does not exist":
                self.log_user_out()
                # self.response.write(user)
                self.redirect('/home')
            else:
                user_id = user.key().id()
                self.log_user_in(str(user_id))
                self.redirect('/profilepage')

        else:
            self.redirect('/home')

class ProfilePageHandler(RequestHandler):
    def get(self):
        if self.user:
            profile = self.user_profile
            if profile == "Entrepreneur":
                self.redirect('/entrepreneur')
            elif profile == "Mentor":
                self.redirect("/mentor")
            elif profile == "Administrator":
                self.redirect("/admin")
            else:
                self.log_user_out()
                self.redirect("/home")

        else:
            self.redirect('/home')

class EntrepreneurPageHandler(RequestHandler):
    def get(self):
        if self.user and self.user_profile == "Entrepreneur":
            user = User.get_by_id(int(self.user_id))
            if user.confirmation_status == "confirmed":
                self.redirect("/search")
            else:
                self.log_user_out()
                self.render('/success_entrepreneur.html')   
        else:
            self.redirect('/home')  

class MentorPageHandler(RequestHandler):
    def get(self):
        if self.user and self.user_profile == "Mentor":
            user = User.get_by_id(int(self.user_id))
            if user.confirmation_status == "confirmed":                
                self.render("editmentorprofile.html", mentor = user)
            else:
                self.log_user_out()
                self.render('/success_entrepreneur.html')   
        else:
            self.redirect('/home') 
    def post(self):
        if self.user and self.user_profile == "Mentor":
            user = User.get_by_id(int(self.user_id))
            action   = self.request.get("action")
            if action == 'edit_profile':
                value = self.request.get('value')
                criteria = self.request.get('criteria')
                perform = self.request.get('action_to_perform')
                category = self.request.get('type')
                result = populate.edit_profile(value, criteria, perform, user, category)
                self.response.write("%s, %s, %s, %s, %s" %(value, criteria, perform, category, result))

            elif action == 'topics':
                return self.render('refreshtopic.html', mentor = user)

class ResourceHandler(RequestHandler):
    def getResources(self):
        resources = Resource.all().order("-created")
        user      = User.get_by_id(int(self.user_id))
        return (resources, user)

    def get(self):
        if self.user and self.user_profile == "Administrator": 
            upload_url    = blobstore.create_upload_url('/upload') 
            resources, user = self.getResources()       
            self.render("administrator/resources.html",
                        upload=upload_url,
                        resources=resources,
                        user=user,
                        user_id=self.user_id)

    def post(self):
        pass

class AdminPageHandler(RequestHandler): 
    def getResources(self):
        resources = Resource.all().order("-created") 
        return resources

    def get(self):
        if self.user and self.user_profile == "Administrator":
            upload_url    = blobstore.create_upload_url('/upload') 
            allmentors    = User.all().filter("user_profile =","Mentor").filter("confirmation_status !=", "confirmed").filter("confirmation_status !=", "declined")
            mentors       = User.all().filter("user_profile =","Mentor").filter("confirmation_status !=", "confirmed").filter("confirmation_status !=", "declined")
            entrepreneurs = User.all().filter("user_profile =","Entrepreneur").filter("confirmation_status !=", "confirmed").filter("confirmation_status !=", "declined")
            applicants    = User.all()
            new_jobs      = Jobs.all()
            admin         = User.get_by_id(int(self.user_id))
            admin_name    = admin.first_name + " " + admin.last_name
            resources      = self.getResources()
            self.render("administrator/dashboard.html",
                        admin=admin_name, 
                        user_id=self.user_id, 
                        entrepreneurs=entrepreneurs, 
                        allmentors=allmentors,
                        mentors=mentors, 
                        applicants=applicants, 
                        jobs=new_jobs, 
                        upload=upload_url,
                        resources=resources
                        )
        else:
            self.render("administrator/login.html")
            populate.create_admin()

    def post(self):        
        action   = self.request.get("action")
        upload_url    = blobstore.create_upload_url('/upload')          
        if action == "signin":
            username    = self.request.get("username")
            password = self.request.get("password")
            authentic_admin = Administrator.log_in_admin(username, password)
            if authentic_admin:
                user_id =  Administrator.all().filter("username =", username).get().user.key().id()
                entrepreneurs = User.all().filter("user_profile =","Entrepreneur").filter("confirmation_status !=", "confirmed").filter("confirmation_status !=", "declined")
                mentors       = User.all().filter("user_profile =","Mentor").filter("confirmation_status !=", "confirmed")
                allmentors    = User.all().filter("user_profile =","Mentor").filter("confirmation_status !=", "confirmed").filter("confirmation_status !=", "declined")             
                applicants    = User.all()
                new_jobs      = Jobs.all()                
                self.log_user_in(str(user_id))
                admin         = User.get_by_id(int(user_id))
                admin_name    = admin.first_name + " " + admin.last_name
                resources      = self.getResources()
                self.render("administrator/dashboard.html",
                            admin=admin_name, 
                            entrepreneurs=entrepreneurs, 
                            allmentors=allmentors, 
                            mentors=mentors, 
                            applicants=applicants,  
                            jobs=new_jobs, 
                            upload=upload_url,
                            resources=resources
                            )
            else:
               self.log_user_out()

        elif action == "confirm":
            try:
                user_id       = self.request.get("user_id")
                admin_action  = self.request.get("data_action")
                state         = self.request.get("state") 
                applicant     = User.get_by_id(int(user_id))

                if admin_action == "confirm":
                    result    = User.confirm(user_id)
                    if state != "restore" and state == "confirm":
                        mail = mailhandler.confirmUserMail(applicant)
                    print mail

                elif admin_action == "decline":
                    result    = User.decline(user_id)
                
                self.response.write(json.dumps({"status":result, 
                                                "user_id":user_id, 
                                                "firstname": applicant.first_name,
                                                "lastname": applicant.last_name 
                                                }))


            except:
                self.response.write(json.dumps({"status":"error","action":"confirm","value":False}))

        elif action == "remove":
            try:
                applicant_id   = self.request.get("user_id")
                applicant      = User.get_by_id(int(applicant_id))
                result         = User.decline(applicant_id)
                if result == "declined":
                    self.response.write(json.dumps({"status":"success","action":"remove","value":True}))
                else:
                    self.response.write(json.dumps({"status":"error","action":"remove","value":False}))
            except:
                self.response.write(json.dumps({"status":"error","action":"remove","value":False}))

        elif action == "delete_user":
            try:
                applicant_id   = self.request.get("user_id")
                applicant      = User.get_by_id(int(applicant_id))
                result         = populate.delete_user(applicant)
                if result == True:
                    self.response.write(json.dumps({"status":"success","action":"remove","value":True}))
                else:
                    self.response.write(json.dumps({"status":"error","action":"remove","value":False}))
            except:
                self.response.write(json.dumps({"status":"error","action":"remove","value":False}))
        else:
            self.response.write(json.dumps({"status":"error","action":"unknown"}))

class EntrepreneurAdminPageHandler(RequestHandler):
    def get(self):        
        if self.user and self.user_profile == "Administrator":            
            user                   = User.get_by_id(int(self.user_id))
            all_entrepreneurs      = User.all().filter("user_profile =", "Entrepreneur")
            new_entrepreneurs      = User.all().filter("user_profile =", "Entrepreneur").filter("confirmation_status !=", "confirmed").filter("confirmation_status !=", "declined")
            approved_entrepreneurs = User.all().filter("user_profile =", "Entrepreneur").filter("confirmation_status =", "confirmed")
            declined_entrepreneurs = User.all().filter("user_profile =", "Entrepreneur").filter("confirmation_status =", "declined")
            self.render("administrator/entrepreneur.html",
                        user=user,
                        new_entrepreneurs=new_entrepreneurs,
                        approved_entrepreneurs=approved_entrepreneurs,
                        all_entrepreneurs=all_entrepreneurs,
                        declined_entrepreneurs=declined_entrepreneurs
                        )

        else:
            self.redirect("/admin")

    def post(self):        
        pass

class MentorAdminPageHandler(RequestHandler):
    def getMentors(self,mentors):        
        if self.user and self.user_profile == "Administrator":
            approved_mentors = []
            for mentor in mentors:
                if mentor.user.confirmation_status == "confirmed":
                    approved_mentors.append(mentor.user)
            return approved_mentors
        

    def get(self):        
        if self.user and self.user_profile == "Administrator":
            new_mentors     = User.all().filter("user_profile =", "Mentor").filter("confirmation_status !=", "confirmed").filter("confirmation_status !=", "declined")
            mentors         = self.getMentors(Program.gql("WHERE program_type=:1", "Subject Area Mentor"))
            mba_mentors     = self.getMentors(Program.gql("WHERE program_type=:1", "MBA Consultant"))
            expert_mentors  = self.getMentors(Program.gql("WHERE program_type=:1", "Expert in residence"))
            senior_mentors  = self.getMentors(Program.gql("WHERE program_type=:1", "Senior advisor"))
            declined_mentors= User.all().filter("user_profile =", "Mentor").filter("confirmation_status =", "declined")
            user            = User.get_by_id(int(self.user_id))
            self.render("administrator/mentor.html",
                                    user=user,
                                    mentors=mentors,
                                    new_mentors=new_mentors,
                                    mba_mentors=mba_mentors,
                                    expert_mentors=expert_mentors,
                                    senior_mentors=senior_mentors,
                                    declined_mentors=declined_mentors, 
                    )
        else:
            self.redirect("/admin")

    def post(self):
        pass

class InboxDefaultHandler(RequestHandler):
    def get(self):
        self.redirect('/messages/inbox')

class InboxHandler(RequestHandler):
    def get(self, category):
        if self.user:
            user = User.get_by_id(int(self.user_id))
            if user.user_profile == "Mentor":
                self.redirect('/mentor')
            elif category == "sent":
                messages =  Message.all().filter('sender =', user).order('-created')  
                self.render('message-inbox.html', user=user, messages=messages, category=category)
            elif category == "inbox":
                messages =  Message.all().filter('receiver =', user).order('-created')  
                self.render('message-inbox.html', user=user, messages=messages, category=category) 
            else:
                self.redirect('/messages')
        else:
            self.redirect('/home')

    def post(self, category):
        user = User.get_by_id(int(self.user_id))
        action = self.request.get('action')
        if action == "change-status":
            status = self.request.get('status')
            message_id = self.request.get('message_id')
            result = Message.change_status(message_id,status)
            self.response.write(result)
        elif action == "delete-message":
            message_id = self.request.get('message_id')
            result = Message.delete_message(message_id)
            self.response.write(result)
        elif action == "display-message":
            msg_id = self.request.get("message_id")
            category = self.request.get("category")
            message = Message.displayMessage(msg_id)
            self.render("view-message.html", message=message, category=category)
            return

class ReplyMessageHandler(RequestHandler):
    def get(self, message_id):
        if self.user:
            user = User.get_by_id(int(self.user_id))
            if user.user_profile == "Entrepreneur" or user.user_profile == "Administrator":
                # self.redirect('/mentor')
                # self.response.write(dir(message))                
                message = Message.get_by_id(int(message_id))
                message.subject = "Re: %s" %(message.subject)
                self.render('message-compose.html', 
                    category="Message Reply", 
                    message=message,
                    user=user)

class MessagePageHandler(RequestHandler):
    def getUser(self):
        if self.user:
            return User.get_by_id(int(self.user_id))
        else:
            self.redirect('/home')

    def returnMessages(self, messages, message_type, user):
        if  message_type == "inbox":
            messages_to_show = messages.filter('receiver =', user).order('-created')
            self.render('refresh-msg.html', messages=messages_to_show)

        elif message_type == "sent":
            messages_to_show = messages.filter('sender =', user).order('-created')   
            self.render('refresh-msg.html', messages=messages_to_show)  

        return

    def getMessages(self, inbox_category, message_type, user):

        messages = Message.all()
        
        if inbox_category == "all":
            messages = Message.all()

        elif inbox_category == "mentors":
            messages = messages.filter("category =", "Mentor")

        elif inbox_category == "applicants":
            messages = messages.filter("category =", "Applicant")

        self.returnMessages(messages, message_type, user)

    def get(self):
        if self.user:
            user = User.get_by_id(int(self.user_id))
            if user.user_profile == "Mentor":
                self.redirect('/mentor')
            else:
                messages =  Message.all().filter('receiver =', user).order('-created')
                compose = False
                self.render('message-center.html', user=user, messages=messages, compose=compose)  
                # self.render('message-inbox.html')    
        else:
            self.redirect('/home')

    def post(self):
        user = User.get_by_id(int(self.user_id))
        action = self.request.get('action')
        if action == "messages":
            inbox_category   = self.request.get('inbox_category')
            message_type     = self.request.get('message_type')
            self.getMessages(inbox_category, message_type, user)
            return

        elif action == "displayMessageContent":
            msg_id  = self.request.get("message_id")
            read_status = self.request.get('read_status')
            message = Message.getMessage(msg_id, read_status)
            self.render("opened-message.html", message=message)
            return

        elif action =="send-message":
            receiver_id = self.request.get('receiver_id')
            receiver    = User.get_by_id(int(receiver_id))
            user = self.getUser()
            messages =  Message.all().filter('receiver =', user).order('-date_sent')
            compose  = True
            self.render('message-center.html', user=user, messages=messages, compose=compose,receiver=receiver)
            return

        elif action == "star":
            status     = self.request.get('status')
            message_id = self.request.get('message_id')
            if status == "false":
                result = Message.unstar(message_id)
            elif status == "true":
                result = Message.star(message_id)
            
            self.response.write(result)

        elif action == "changeMessageReadStatus":
            status     = self.request.get('status')
            message_id = self.request.get('message_id')
            result =  Message.change_status(message_id,status)
            self.response.write(result)

        elif action == "delete-message":
            message_id = self.request.get('message_id')
            result     = Message.delete_message(message_id)
            self.response.write(result)

        elif action == 'sendReplyMessage':
            msg_id         = self.request.get('msg_id')
            subject        = self.request.get('subject')
            recipient_name = self.request.get('recipient_name')
            msg            = self.request.get('msg')
            msg_raw        = self.request.get('msg_raw')
            notify         = self.request.get('notify')
            user           = self.getUser()
            replied        = mailhandler.sendReply(user, msg_id, msg, msg_raw, subject, recipient_name, notify)
            self.response.write(replied)

        else:
            self.response.write("Something went wrong somewhere!")

class ComposeNewMessageHandler(RequestHandler):
    def getUser(self, user_id):
        return User.get_by_id(int(user_id))

    def get(self, user_id):
        if self.user:
            user = User.get_by_id(int(self.user_id))
            if user.user_profile == "Entrepreneur" or user.user_profile == "Administrator":   
                message = {}     
                message['receiver'] = self.getUser(user_id)
                message['sender'] = self.getUser(self.user_id)
                message['subject'] = "Subject: Seeking advice about email marketing"
                self.render('message-compose.html', 
                    category="Message Compose", 
                    message=message,
                    user=user)

    
    def post(self, user_id):
        def getMessage(user, recipient):
            #dict to hold message
            message                     = {}

            #determining how message will be saved
            message['msg_type']         = "new message to"
            message['category']         = self.request.get("type-of-email")
            message['receiver_profile'] = recipient.user_profile #has to be the email of the receiver not the sender. Must change this
            message['receiver']         = recipient
            message['sender']           = user

            #message details to be sent through mandrill
            message['sender_email']       = user.alias
            message['sender_name']        = user.first_name +" "+ user.last_name
            message['receiver_email']     = recipient.email 
            message['receiver_name']      = recipient.first_name +" "+ recipient.last_name
            message['subject']            = self.request.get("subject")
            message['content']            = self.request.get("message")
            message['receiver_id']        = recipient.key().id()
            message['notification_email'] = self.request.get("notify-email")
            message['reply_to']           = user.alias #sender alias  
            message['date']               = strftime("%a, %d %b %Y %X +0000", gmtime())  

            return message

        if self.user:
            user =  self.getUser(self.user_id)
            recipient_id = self.request.get("recipient")
            recipient = self.getUser(recipient_id)
            message = getMessage(user, recipient)
            message_status = mailhandler.composeNewMail(message) 
            print message_status
            print type(message_status)
            # self.response.write(message_status)
            # if message_status ==
            self.redirect("/messages/sent")

class ComposeMessageHandler(RequestHandler):
    def get(self):
        if self.user:
            user = User.get_by_id(int(self.user_id))
            self.render("compose-message22.html", user=user)
        else:
            self.redirect('/home')

    def post(self):
        if self.user:
            user = User.get_by_id(int(self.user_id))
            action = self.request.get('action')
            if action == "sendMessageAjax":
                
                messageSTRING               = self.request.get('message') #fecthing message sent by ajax
                messageJSON                 = json.loads(messageSTRING)
                receiver_id                 = messageJSON[3]['receiver_id']
                recipient                   = User.get_by_id(int(receiver_id))
            
                #dict to hold message
                message                     = {}

                #determining how message will be saved
                message['msg_type']         = "new message to"
                message['category']         = messageJSON[0]['type'] 
                message['receiver_profile'] = recipient.user_profile #has to be the email of the receiver not the sender. Must change this
                message['receiver']         = recipient
                message['sender']           = user

                #message details to be sent through mandrill
                message['sender_email']       = user.alias
                message['sender_name']        = user.first_name +" "+ user.last_name
                message['receiver_email']     = recipient.email 
                message['receiver_name']      = recipient.first_name +" "+ recipient.last_name
                message['subject']            = messageJSON[1]['subject']
                message['content']            = messageJSON[2]['content']
                message['receiver_id']        = messageJSON[3]['receiver_id']
                message['notification_email'] = messageJSON[4]['notification_email']
                message['reply_to']           = user.alias #sender alias  
                message['date']               = strftime("%a, %d %b %Y %X +0000", gmtime())  

                ################################## working on this at the moment #############################
                # print message
                #confirming email was sent
                # message_status              = mailhandler.outBoundMail(message)   
                # msg                         = Message.create(message)
                message_status                = mailhandler.composeNewMail(message) 
                # self.response.write(message) 
                print message_status
                self.response.write(message_status)

            else:
                self.redirect('/compose')
        else:
            self.redirect('/compose')    

class SearchPageHandler(RequestHandler):
    def unique_result(self,array):
        unique_results = []
        for obj in array:
            if obj not in unique_results:
                unique_results.append(obj)
        return unique_results
    def returnCriterias(self,result):
        returnedTopics = []
        for query in result:
            for query.topic in query:
                user = query.topic.program.user
                if user.confirmation_status == "confirmed":
                    userJSON = {}
                    userJSON["name"]    = user.first_name + " "+user.last_name
                    userJSON["id"]      = str(user.key().id())
                    userJSON["summary"] = user.programs[0].mini_bio
                    userJSON["profile"] = user.user_profile
                    userJSON["image"]   = user.picture

                    logged_user                 = User.get_by_id(int(self.user_id))
                    status                      = Favorite.check(logged_user, userJSON["id"])
                    userJSON["data_fav_status"] = status["favorite"]
                    userJSON["data_fav_src"]    = status["src"]             

                    returnedTopics.append(userJSON) 
        return returnedTopics

    def returnSectors(self,result):
        returnedSectors = []
        for query in result:
            for query.sector in query:
                user = query.sector.program.user
                if user.confirmation_status == "confirmed":
                    userJSON = {}
                    userJSON["name"]    = user.first_name + " "+user.last_name
                    userJSON["id"]      = str(user.key().id())
                    userJSON["summary"] = user.programs[0].mini_bio
                    userJSON["profile"] = user.user_profile
                    userJSON["image"]   = user.picture

                    logged_user                 = User.get_by_id(int(self.user_id))
                    status                      = Favorite.check(logged_user, userJSON["id"])
                    userJSON["data_fav_status"] = status["favorite"]
                    userJSON["data_fav_src"]    = status["src"]

                    returnedSectors.append(userJSON) 
        return returnedSectors

    def get(self):
        if self.user:
            user            = User.get_by_id(int(self.user_id))
            if user.user_profile == "Mentor":
                self.redirect('/mentor')
            else:
                totalFavorites  = Favorite.gql("WHERE user=:1", user).count()
                self.render("/search/new_search.html", favorites = totalFavorites)
        else:
            self.redirect('/home')
    def post(self):
            action = self.request.get('action')
            if action =="largeSearch":
                totalResults = []
                foundTopics  = []
                successTopics = []
                successSectors = [] 
                foundSectors = []
                sector_count = len(self.request.get('sectors'))
                topic_count  = len(self.request.get('topics'))
                if topic_count > 2:
                    topicSTRING  = self.request.get('topics')
                    topicUTF     = json.loads(str(topicSTRING))
                    topicJSON    = jsonString.convert(topicUTF)  
                    for topic in topicJSON:
                        self.query = Topic.all().filter("value = ",topic.get('value'))
                        foundTopics.append(self.query)
                    successTopics =  self.returnCriterias(foundTopics)
                if sector_count > 2:
                    sectorSTRING = self.request.get('sectors')
                    sectorUTF    = json.loads(str(sectorSTRING))
                    sectorJSON   = jsonString.convert(sectorUTF)
                    for sector in sectorJSON:
                        self.query = Sector.all().filter("value = ", sector.get('value'))
                        foundSectors.append(self.query)
                    successSectors = self.returnSectors(foundSectors)

                totalResults = successSectors + successTopics
                finalResults = self.unique_result(totalResults)

                self.response.write(json.dumps(finalResults))

            elif action == "getFullProfile":
                user_id = self.request.get("user_id")
                user    = User.get_by_id(int(user_id))
                user_profile = {}
                user_profile["user"]             = m2json.to_dict(user)
                user_profile["user"]["user_id"]  = user_id


                logged_user                             = User.get_by_id(int(self.user_id))
                status                                  = Favorite.check(logged_user, user_id)
                user_profile["user"]["user_profile"]    = user.user_profile
                user_profile["user"]["data_fav_status"] = status["favorite"]
                user_profile["user"]["data_fav_src"]    = status["src"]

                rating                                  = Rating.check(logged_user, user_id)
                user_profile["user"]["rating"]          = rating
                
                if user.educations:
                    user_profile["educations"]   = m2json.gql_json_parser(user.educations)

                if user.positions:
                    user_profile["positions"]    = m2json.gql_json_parser(user.positions)

                if user.skills:
                    user_profile["skills"]       = m2json.gql_json_parser(user.skills)

                if user.comments_received:
                    user_profile["logged_user_comment"] = Comment.check({"entity_id":user_id, "commentor_id":self.user_id})
                    user_profile["comments_received"]   = []
                    for comments_received in user.comments_received:
                        received = {}
                        received['user']           = comments_received.user.first_name + " " + comments_received.user.last_name
                        received['resource']       = comments_received.resource
                        received['entity_id']      = comments_received.entity_id
                        received['comment_id']     = comments_received.key().id()
                        received['commentor']      = comments_received.commentor_name
                        received['commentor_name'] = comments_received.commentor_name
                        received['commentor_id']   = comments_received.commentor_id
                        received['content']        = comments_received.content
                        received['created']        = m2json.get_milliseconds(comments_received.created)
                        received["rating"]         = Rating.check(comments_received.commentor, comments_received.entity_id)
                        user_profile["comments_received"].append(received)

                if user.programs:
                    user_profile["program"]      = m2json.gql_json_parser(user.programs)

                if user.programs[0].topics:
                    user_profile["topics"]       = m2json.gql_json_parser(user.programs[0].topics)

                if user.programs[0].sectors:
                    user_profile["sectors"]      = m2json.gql_json_parser(user.programs[0].sectors)
                self.response.write(json.dumps(user_profile))

            elif action == "favorite":
                favorite_action = self.request.get('favorite_action')
                favorite_type   = self.request.get('favorite_type')
                favorite_id     = self.request.get('favorite_id')

                user            = User.get_by_id(int(self.user_id))
                result          = {}

                if favorite_action == "unlike":
                    totalFavorites = Favorite.gql("WHERE user=:1", user).count()
                    result         = Favorite.delete(user, favorite_type, favorite_id)
                    message        = {"message": result, "value": totalFavorites-1}
                    self.response.write(json.dumps(message))

                elif favorite_action == "like":
                    totalFavorites = Favorite.gql("WHERE user=:1", user).count()
                    result         = Favorite.create(user, favorite_type, favorite_id)
                    message        = {"message": result, "value": totalFavorites+1}
                    self.response.write(json.dumps(message))

                else:
                    result["message"] = "error"
                    result["value"]   = "wrong command"
                    self.response.write(favorite_action)

            elif action == "rate":
                rating_type   = self.request.get('rating_type')
                rating_id     = self.request.get('rating_id')
                rating_value  = self.request.get('rating_value')

            
                user          = User.get_by_id(int(self.user_id))
                result        = {}
                result        = Rating.rate(user, rating_type, rating_id, rating_value)
                message       = result

                self.response.write(json.dumps(message))

            elif action == "comment":
                comment                 = self.request.get("comment")
                comment                 = json.loads(comment)
               
                user                    = User.get_by_id(int(self.user_id))
                comment['commentor_id'] = self.user_id
                comment['commentor']    = user
                
                if comment.get('type')  == "user":
                    comment['entity']   = User.get_by_id( int( comment.get('entity_id') ) )
                else:
                    comment['entity']   = Resource.get_by_id( int( comment.get('entity_id') ) )
                
                comment_action          = comment.get("comment_action")                 

                if comment_action == "new":
                    result               = Comment.create(comment)
                    comment['status']    = result.get('status')
                    comment["comment_id"]     = result.get('value')
                    comment['entity']    = None 
                    comment['commentor'] = user.first_name + " " + user.last_name
                    self.response.write(json.dumps(comment)); 
                elif comment_action == "delete":
                    result  = Comment.delete(comment)
                    comment['status']    = result.get('status')
                    comment["comment_id"]     = result.get('value')
                    comment['entity']    = None 
                    comment['commentor'] = user.first_name + " " + user.last_name 
                    self.response.write(json.dumps(comment)); 
                elif comment_action == "edit":
                    result  = Comment.edit(comment)
                    comment['status']    = result.get('status')
                    comment["comment_id"]     = result.get('value')
                    comment['entity']    = None 
                    comment['commentor'] = user.first_name + " " + user.last_name
                    self.response.write(json.dumps(comment));   
            else:
                result["message"] = "error"
                result["value"]   = "wrong command"
                self.response.write(rating_action)

class SubmitHandler(webapp2.RequestHandler):
    def get(self):
        upload_url = blobstore.create_upload_url('/upload')
        self.response.out.write('<html><body>')
        self.response.out.write('<form action="%s" method="POST" enctype="multipart/form-data">' % upload_url)
        self.response.out.write("""Upload File: <input type="file" name="file"><br> <input type="submit" name="submit" value="Submit"> </form></body></html>""")


class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    def getTags(self):
        industry     = json.loads(self.request.get("industry"))
        expertise    = json.loads(self.request.get("expertise"))
        return (industry, expertise)

    def post(self):
        try:
            user_id             = self.request.get("user_id")
            title               = self.request.get("title")
            description         = self.request.get("description")
            industry, expertise = self.getTags()
            upload_files        = self.get_uploads('file')  # 'file' is file upload field in the form
            blob_info           = upload_files[0]
            entity              = Resource.create(user_id, blob_info.key(), title, description, industry, expertise)
            key                 = entity.resource_key.key()
            self.response.write("resource uploaded successfully. <a href='/admin'>Click here to go back</a>")
        except:
            self.response.write("Something went wrong somewhere and it's your fault.")

class ServeHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, resource):
        resource = str(urllib.unquote(resource))
        blob_info = blobstore.BlobInfo.get(resource)
        self.send_blob(blob_info)

class SignoutPageHandler(RequestHandler):
    def get(self):
        if self.user and self.user_profile != "Administrator":
            self.log_user_out()
            self.redirect("/home")
        elif self.user and self.user_profile == "Administrator":
            self.log_user_out()
            self.redirect("/admin")
        else:
            self.log_user_out()
            self.redirect("/home")

class DeleteHandler(RequestHandler):
    def get(self):
        self.redirect("/home")
        # db.delete(Administrator.all())
        # db.delete(Comment.all())
        # db.delete(Discovery.all())
        # db.delete(Education.all())
        # db.delete(Entrepreneur.all())
        # db.delete(Favorite.all())
        # db.delete(Jobs.all())
        # db.delete(Message.all())
        # db.delete(Position.all())
        # db.delete(Program.all())
        # db.delete(Rating.all())
        # db.delete(Resource.all())
        # db.delete(Sector.all())
        # db.delete(Skills.all())
        # db.delete(Subscriber.all())
        # db.delete(Topic.all())
        # db.delete(User.all())

app = webapp2.WSGIApplication([
                                ('/', MainPage), 
                                ('/home', HomePageHandler),
                                ("/programs",ProgramsHandler), 
                                ('/profilepage', ProfilePageHandler),
                                ('/loginpage', LoginPageHandler),
                                ('/entrepreneur', EntrepreneurPageHandler),
                                ('/mentor', MentorPageHandler),
                                ("/admin", AdminPageHandler),
                                ("/admin/entrepreneur", EntrepreneurAdminPageHandler),
                                ("/admin/mentor", MentorAdminPageHandler),
                                ("/admin/resources", ResourceHandler),
                                ('/serve/([^/]+)?', ServeHandler),
                                ("/submit", SubmitHandler),
                                ('/upload', UploadHandler),
                                # ('/messages/compose', ComposeNewMessageHandler),
                                ('/messages/compose/(\d+)', ComposeNewMessageHandler),
                                # ('/messages', MessagePageHandler),
                                ('/messages', InboxDefaultHandler),
                                ('/messages/([^/]+)?', InboxHandler),
                                ('/messages/reply/(\d+)', ReplyMessageHandler),
                                # ('/compose', ComposeMessageHandler),
                                ("/search", SearchPageHandler),
                                ("/delete", DeleteHandler),
                                ('/signupmentor', MentorSignUpPageHandler),
                                ('/signupentrepreneur', EntrepreneurSignUpPageHandler),
                                ('/signin/mentor', LogInMentor),
                                ('/signup/entrepreneur', SignUpEntrepreneur),
                                ('/signup/mentor', SignUpMentorHandler),
                                ('/signin', SignInEntrepreneur),
                                ('/signin/entrepreneur', LogInEntrepreneur),
                                ("/signout",SignoutPageHandler)
                                # ('/confirm.*',ConfirmPageHandler),
                                # ('/signup/mentor', SignUpMentor),
                                # ('/signup', SignUpEntrepreneur),
                                # ('/signupapplicant', ApplicantSignUpPageHandler),
                              ]
                              , debug = True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()   


