from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from time import gmtime, strftime
import exceptions
from models import *
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
from google.appengine.api import mail
import jsonString

template_dir = "templates"
jinja_env    = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

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
   


class HomePageHandler(RequestHandler):
    def get(self):
        self.render('newHome.html') 

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
            # http://api.linkedin.com/v1/people/~/picture-urls::(original)


            #using access token to fetch user data from linkedIn  
            userprofile          = urllib.urlopen('https://api.linkedin.com/v1/people/~:(id,first-name,last-name,location:(name),summary,industry,public-profile-url,positions,recommendations-received,skills:(id,skill),educations:(id,school-name,field-of-study,start-date,end-date,degree,activities,notes),twitter-accounts,picture-url,email-address)?format=json&oauth2_access_token=%s' %(token['access_token']))
            userdata             = json.loads(userprofile.read())
            profilepic           = urllib.urlopen('https://api.linkedin.com/v1/people/~/picture-urls::(original)?format=json&oauth2_access_token=%s' %(token['access_token'])) 
            bigPic               = json.loads(profilepic.read())
            userdata["big_pic"]  = bigPic['values'][0]
            userdata             = jsonString.convert(userdata)
            #rendering form for new mentor to fill
            self.render('mentor/mentorsignupform.html', user_data=json.dumps(userdata))
            # self.render('mentor/mentorsignupform.html', user_data=json.dumps(userdata), email=userdata['emailAddress'], summary=userdata.get('summary'))
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
                    message     = json.dumps({"message":"success", "firstname":user.first_name, "lastname":user.last_name})
                    self.log_user_out()
                    self.response.write(message)
########################################### need to send alert to admin for confirmation of new user ####################################################
            # except:
            #     self.response.write("Something seems to have gone wrong.")
        # else:
        #     self.redirect('/home')

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
                # print userdata
                if user=='User already exists':
                    self.log_user_out()
                    self.response.write("User already exists.")
                else:
                    user_id = user.key().id()
                    # confirm_user = User.confirm(user_id)
                    self.log_user_in(str(user_id))
                    mail_status = mailhandler.requestMail(user)
                    confirmation_msg  = "Your account has been successfully created and is pending approval"
                    self.log_user_out()
                    self.response.write(confirmation_msg)
########################################### need to send alert to admin for confirmation of new user ####################################################
            else:
                self.redirect("/home")         
        except:
            self.response.write("Something seems to have gone wrong.")
  
#authorizes and fetches job applicant details from linkedin
#further redirects to home when form is successfully filled
#sends alert to admin for confirmation of new job applicant
class ApplicantSignUpPageHandler(RequestHandler): 
    def get(self):
        authorization_code = self.request.get('code')
        state              = self.request.get('state')
        try:
            result         = urllib.urlopen('https://www.linkedin.com/uas/oauth2/accessToken?grant_type=authorization_code&code=%s&redirect_uri=%s&client_id=%s&client_secret=%s' %(authorization_code,Redirect_uri_applicant,API_Key,Secret_Key))
            
            if result.code == 200 and state == State:
                token       = json.loads(result.read())   
                userprofile = urllib.urlopen('https://api.linkedin.com/v1/people/~:(id,first-name,last-name,location:(name),summary,industry,positions,recommendations-received,skills:(id,skill),educations:(id,school-name,field-of-study,start-date,end-date,degree,activities,notes),twitter-accounts,picture-url,email-address)?format=json&oauth2_access_token=%s' %(token['access_token']))
                userdata    = json.loads(userprofile.read())
                profilepic           = urllib.urlopen('https://api.linkedin.com/v1/people/~/picture-urls::(original)?format=json&oauth2_access_token=%s' %(token['access_token'])) 
                bigPic               = json.loads(profilepic.read())
                userdata["big_pic"]  = bigPic['values'][0]
                self.render('applicant/jobapplicantform.html', user_data=json.dumps(userdata))
            else:
                self.redirect('/home')
        except: 
            self.response.write("Something seems to have gone wrong.")

    def post(self):
        action = self.request.get('action')
        if action == "submit_application":
            try:
                user_data = json.loads(self.request.get('user_data'))
                user      = populate.create_user(user_data, "Job Applicant")
                if user=="User already exists":
                    self.log_user_out()
                    message  = json.dumps({"message":"error", "value":user})
                    self.response.write(message)
                else:
                    programUTF  = json.loads(self.request.get('program')) 
                    programJSON = jsonString.convert(programUTF)  
                    program     = populate.create_program(user, programJSON)
                    
                    mail_status = mailhandler.requestMail(user)
                    message     = json.dumps({"message":"success", "firstname":user.first_name, "lastname":user.last_name})
                    self.log_user_out()
                    self.response.write(message)
########################################### need to send alert to admin for confirmation of new user ####################################################
            except:
                self.response.write("Something seems to have gone wrong.")

        else:
            self.redirect('/home')



class LoginPageHandler(RequestHandler):
    def get(self):       
        authorization_code = self.request.get('code')
        state              = self.request.get('state')
        result             = urllib.urlopen('https://www.linkedin.com/uas/oauth2/accessToken?grant_type=authorization_code&code=%s&redirect_uri=%s&client_id=%s&client_secret=%s' %(authorization_code,Redirect_uri_log_in,API_Key,Secret_Key))
        
        if result.code == 200 and  state== State :
            token        = json.loads(result.read())   
            userprofile  = urllib.urlopen('https://api.linkedin.com/v1/people/~:(id,first-name,last-name,email-address)?format=json&oauth2_access_token=%s' %(token['access_token']))
            userdata     = json.loads(userprofile.read()) 
            user         = populate.authenticate(userdata)

            if user == "User does not exist":
                self.log_user_out()
                self.response.write(user)
            else:
                user_id = user.key().id()
                self.log_user_in(str(user_id))
                self.redirect('/profilepage')

        # else:
            # self.redirect('/home')
                
    # def post(self):
    #     self.response.write('')


class ProfilePageHandler(RequestHandler):
    def get(self):
        if self.user:
            profile = self.user_profile
            if profile == "Entrepreneur":
                self.redirect('/entrepreneur')
            else:
                self.log_user_out()
                self.response.write('This is not the page you are looking for')
        else:
            self.redirect('/home')

class EntrepreneurPageHandler(RequestHandler):
    def get(self):
        if self.user:
            user = User.get_by_id(int(self.user_id))
            if user.confirmation_status == "confirmed":
                self.redirect("/messages")
            else:
                self.response.write('Your account has been successfully created and is pending approval')
                self.log_user_out()
        else:
            self.response.write(self.response.write("Error Page comes Here"))
            self.redirect('/home')    

    def post(self):
        if self.user:
            user         = User.get_by_id(int(self.user_id))
            company_name = self.request.get("company_name")
            designation  = self.request.get("designation")
            website      = self.request.get("website")
            entrepreneur = Entrepreneur.create(user,company_name,designation,website)
            if entrepreneur:
                self.redirect("/search")

class AdminPageHandler(RequestHandler):
    def get(self):
        new_users = User.all().filter("confirmation_status !=", "confirmed")
        self.render("admin/admin.html", users = new_users)

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
            messages =  Message.all().filter('receiver =', user).order('-created')
            compose = False
            self.render('message-center.html', user=user, messages=messages, compose=compose)      
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
                print result
                self.response.write(result)
            elif status == "true":
                result = Message.star(message_id)
                print result
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
            self.response.write("bingi error pai!!")

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
            # if action == 'send_message':
            #     message = {}
            #     message['sender_address']    = user.email
            #     message['sender_name']       = user.first_name +" "+ user.last_name
            #     message['receiver_name']     = "Elorm Adjaho"
            #     message['receiver_address']  = "elormm@hotmail.com"          
            #     message['receiver_profile']  = "Mentor"
            #     message['category']          = self.request.get('category')
            #     message['msg_type']          = self.request.get('msg_type')
            #     message['subject']           = self.request.get('subject')
            #     message['content']           = self.request.get('content')
            #     message['reply_to']          = user.alias
            #     new_msg = Message.create(user,message)
            #     self.response.write(new_msg)
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

################################## working on this at the moment #############################3
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

class ConfirmPageHandler(RequestHandler):
    def get(self):
        if self.user:
            userState = self.confirmation_status
            user_profile = access.confirmation.get(self.user_profile)
            if userState != "confirmed":
                self.redirect("/%s" %(user_profile))
        else:
            self.redirect('https://www.linkedin.com/uas/oauth2/authorization?response_type=code&client_id=%s&scope=%s&state=%s&redirect_uri=%s' %(API_Key,Scope_log_in,State,Redirect_uri_log_in))

    def post(self):
        pass

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
            totalFavorites  = Favorite.gql("WHERE user=:1", user).count()
            self.render("/search/new_search.html", favorites = totalFavorites)
        else:
            self.redirect('/home')
    def post(self):
            action = self.request.get('action')
            if action =="largeSearch":
            # try:
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

                # print "================================================================="
                totalResults =successSectors + successTopics
                finalResults  = self.unique_result(totalResults)
                # print finalResults
                # print "================================================================="        
                self.response.write(json.dumps(finalResults))

            # except:
            #     self.response.write("u don 4k up")
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

          


class SignoutPageHandler(RequestHandler):
    def get(self):
        if self.user:
            self.log_user_out()
            self.redirect("/home")
        else:
            self.log_user_out()
            self.redirect("/home")

class DeleteHandler(RequestHandler):
    def get(self):
        self.redirect("/home")
        # db.delete(User.all())
        # db.delete(Entrepreneur.all())
        # db.delete(Skills.all())
        # db.delete(Education.all())
        # db.delete(Position.all())
        # db.delete(Program.all())
        # db.delete(Topic.all())
        # db.delete(Sector.all())

app = webapp2.WSGIApplication([
                                ('/', MainPage), 
                                ('/home', HomePageHandler), 
                                ('/profilepage', ProfilePageHandler),
                                ('/loginpage.*', LoginPageHandler),
                                ('/entrepreneur.*', EntrepreneurPageHandler),
                                ('/signupmentor', MentorSignUpPageHandler),
                                ('/signupentrepreneur', EntrepreneurSignUpPageHandler),
                                ('/signupapplicant', ApplicantSignUpPageHandler),
                                ("/admin", AdminPageHandler),
                                ('/messages', MessagePageHandler),
                                ('/compose', ComposeMessageHandler),
                                ('/confirm.*',ConfirmPageHandler),
                                ("/search", SearchPageHandler),
                                ("/signout",SignoutPageHandler),
                                ("/delete", DeleteHandler)
                              ]
                              , debug = True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()   


