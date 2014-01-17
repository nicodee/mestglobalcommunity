import logging
import webapp2
import exceptions
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
from models import *
import mailhandler

def getEmail(value):
    try:
        logging.info(value)
        logging.info(type(value))
        value = str(value).split("<")
        if isinstance(value, list):
            value_email = value[1].strip(">")
            value_name  = value[0].split(" ")
            return value_email
        else:
            return value.strip("<").strip(">")
            logging.info(value)
    except:
        return value[0]

class LogSenderHandler(InboundMailHandler):
    def receive(self, mail_message):
        user = ''
        def getSender():
            try:
                SENDER = getEmail(mail_message.sender)
                logging.info(SENDER)
                sender_one = User.gql("WHERE email=:1", SENDER)
                sender_two = User.gql("WHERE alias=:1", SENDER)
                print "============="
                print sender_two.count()
                print "============="
                if sender_one.count()==1:
                    return sender_one.get()
                elif sender_two.count()==1:
                    return sender_two.get()          
            except exceptions.AttributeError:
                return mail_message.sender
        def getRecipient():
            try:
                RECEIVER = getEmail(mail_message.to)
                logging.info(RECEIVER)
                receiver_one = User.gql("WHERE email=:1", RECEIVER)
                receiver_two = User.gql("WHERE alias=:1", RECEIVER)
                if receiver_one.count()==1:
                    user = receiver_one.get()
                    return receiver_one.get()
                elif receiver_two.count()==1:
                    return receiver_two.get()          
            except exceptions.AttributeError:
                return None 
        def getDate():
            try:
                return mail_message.date
            except exceptions.AttributeError:
                return "None"   
        def getSubject():
            try:
                return mail_message.subject
            except exceptions.AttributeError:
                return "None"
        def getContent():
            try:
                plaintext_bodies = mail_message.bodies('text/plain')
                html_bodies = mail_message.bodies('text/html')

                for content_type, body in html_bodies:
                    decoded_html = body.decode()
                    return decoded_html
            except exceptions.AttributeError:
                return "None"                
        def getCC():
            try:
                return mail_message.cc
            except exceptions.AttributeError :
                return "None"
        def getSenderCategory(sender):
            return sender.user_profile

        message                   = {}
        message["sender"]         = getSender()
        message["category"]       = getSenderCategory(getSender())
        message["receiver"]       = getRecipient()
        message["date"]           = getDate()
        message["cc"]             = getCC()
        message["content"]        = getContent()
        message["subject"]        = getSubject()
        message["sender_email"]   = getEmail(mail_message.sender)
        message["receiver_email"] = getEmail(mail_message.to)
        message["type"]           = "incoming"

        mailhandler.notifyEntrepreneur(message)
        new_message = Message.create(message)
        logging.info(new_message)

app = webapp2.WSGIApplication([LogSenderHandler.mapping()], debug=True)