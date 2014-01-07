from models import User, Message
from time import gmtime, strftime
import mandrill
import exceptions
import mailContent
import access
KEY = access.mandrill_key 

#sending confirmation mail
def populate_confirmation_message(user):
    user_status      = user.confirmation_status
    user_name        = user.first_name + " " + user.last_name
    confirmation_url = access.confirmation_url  %(user_status)
    message = {"sender_email"     : "admin@mestglobalcommunity.appspotmail.com" ,
                "sender_name"      : "Admin",
                "receiver_email"   : user.email,
                "receiver_name"    : user_name,
                "subject"          : "Welcome to %s" %(user_name),
                "tag"              : "Signup Confirmation",
                "reply_to"         : "<no-reply>@mestglobalcommunity.appspotmail.com",
                "confirmation_url" : confirmation_url
                }
    return message

def confirmationMail(user):
    message          = populate_confirmation_message(user) 
    from_email       = message.get("sender_email")
    from_name        = message.get("sender_name")
    to_email         = message.get("receiver_email")
    to_name          = message.get("receiver_name")
    subject          = message.get("subject")
    tags             = message.get("tag")
    html             = mailContent.confirmation
    reply_to         = message.get("reply_to")
    confirmation_url = message.get("confirmation_url")

    return sendConfirmationMail(from_email, from_name, to_email, to_name, subject, tags, html, reply_to, confirmation_url)


def sendConfirmationMail(from_email, from_name, to_email, to_name, subject, tags, html, reply_to, confirmation_url):
    try:
        mandrill_client = mandrill.Mandrill(KEY)
        message = {'auto_html': True,
         'auto_text': True,
         'from_email': from_email,
         'from_name': from_name,
         'global_merge_vars': [{'content': 'merge1 content', 'name': 'merge1'}],
         'headers': {'Reply-To': reply_to},
         'html': html,
         'important': True,
         'inline_css': True,
         'merge': True,
         'merge_vars': [{'rcpt': to_email,
                         'vars': [
                                    {'name': 'user', 'content': to_name},
                                    {'name': 'email', 'content': to_email},
                                    {'name':'confirmationurl', 'content': confirmation_url}
                                  ]
                        }],
         'metadata': {'website': 'www.mestglobalcommunity.appspot.com'},
         'preserve_recipients': None,
         'recipient_metadata': [{'rcpt': to_email,
                                 'values': {'user_id': 123456}}],
         'signing_domain': None,
         'subject': subject,
         'tags': [tags],
         'text': "text",
         'to': [{'email': to_email}],
         'track_clicks': True,
         'track_opens': True,
         'tracking_domain': None,
         'url_strip_qs': None}
        result = mandrill_client.messages.send(message=message, async=False, ip_pool='Main Pool')
        return result


    except mandrill.Error, e: 
        return 'A mandrill error occurred: %s - %s' % (e.__class__, e)
#confirmation mail ends here


#sending an outbound mail. From entrepreneur to mentor or job applicant

def outBoundMail(message):

    from_email = message.get("sender_email")
    from_name  = message.get("sender_name")
    to_email   = message.get("receiver_email")
    # to_email   = "kaizzenn@yahoo.com"
    to_name    = message.get("receiver_name")
    subject    = message.get("subject")
    html       = message.get("content")
    reply_to   = message.get("reply_to")
    tags       = "Outbound Mail"

    merge      = False
    variables  = None 
    return sendOutboundMail(from_email, from_name, to_email, to_name, subject, html, tags, reply_to, variables, merge)
    
    
def sendOutboundMail(from_email, from_name, to_email, to_name, subject, html, tags, reply_to, variables, merge):
    try:
        mandrill_client = mandrill.Mandrill(KEY)
        message = {'auto_html': True,
         'auto_text': True,
         'from_email': from_email,
         'from_name': from_name,
         'global_merge_vars': [{'content': 'merge1 content', 'name': 'merge1'}],
         'headers': {'Reply-To': reply_to},
         'html': html,
         'important': True,
         'inline_css': True,
         'merge': merge,
         'merge_vars': [{'rcpt': to_email, 'vars': variables}],
         'metadata': {'website': 'www.mestglobalcommunity.appspot.com'},
         'preserve_recipients': None,
         'recipient_metadata': [{'rcpt': to_email,
                                 'values': {'rcpt_name': to_name}
                                 }],
         'signing_domain': None,
         'subject': subject,
         'tags': [tags],
         'text': html,
         'to': [{'email': to_email}],
         'track_clicks': True,
         'track_opens': True,
         'tracking_domain': None,
         'url_strip_qs': None}
        result = mandrill_client.messages.send(message=message, async=False, ip_pool='Main Pool')
        print result[0].get("_id")
        return result


    except mandrill.Error, e: 
        return 'A mandrill error occurred: %s - %s' % (e.__class__, e)
#outbound mail ends here

def getAdminDetails():
    recipient    = {}

    recipient['name']  = "Administration" 
    recipient['email'] = "nnutsukpui@gmail.com"
    # #<incubator.mgmt@meltwater.org>
    # recipient['alias'] = "<no-reply>@mestglobalcommunity.appspotmail.com"
    # recipient['alias'] = "incubator.mgmt@meltwater.org"
     # <incubator.mgmt@meltwater.org>


    # recipient['name']  = "Anirudh Narla" 
    # recipient['email'] = "anirudh@meltwater.org"
    recipient['alias'] = "<no-reply>@mestglobalcommunity.appspotmail.com"

    return recipient

user_role = {"Entrepreneur": "an Entrepreneur", "Mentor": "a Mentor", "Job Applicant": "a Freelancer"}

def requestMail(user):
    new_user_name    = user.first_name + " " + user.last_name
    new_user_role    = user_role.get(user.user_profile)

    from_email       = "admin@mestglobalcommunity.appspotmail.com" 
    from_name        = "Signup Administration"

    recipient        = getAdminDetails();

    to_email         = recipient.get("email")
    to_name          = recipient.get("name")

    subject          = "Request For Confirmation"
    html             = mailContent.request
    reply_to         = recipient.get("alias")
    tags             = "Request For Confirmation"

    confirmation_url = "http://mestglobalcommunity.appspot.com/admin"

    variables        = [{'name': 'username', 'content': new_user_name}, 
                        {'name': 'role', 'content': new_user_role }, 
                        {'name':'confirmation_url', 'content': confirmation_url}]

    print sendRequestMail(from_email, from_name, to_email, to_name, subject, html, tags, reply_to, variables)


def sendRequestMail(from_email, from_name, to_email, to_name, subject, html, tags, reply_to, variables):
    try:
        mandrill_client = mandrill.Mandrill(KEY)
        message = {'auto_html': True,
         'auto_text': True,
         'from_email': from_email,
         'from_name': from_name,
         'global_merge_vars': [{'content': 'merge1 content', 'name': 'merge1'}],
         'headers': {'Reply-To': reply_to},
         'html': html,
         'important': True,
         'inline_css': True,
         'merge': True,
         'merge_vars': [{'rcpt': to_email, 'vars': variables}],
         'metadata': {'website': 'www.mestglobalcommunity.appspot.com'},
         'preserve_recipients': None,
         'recipient_metadata': [{'rcpt': to_email,
                                 'values': {'user_id': 123456}}],
         'signing_domain': None,
         'subject': subject,
         'tags': [tags],
         'text': "text",
         'to': [{'email': to_email}],
         'track_clicks': True,
         'track_opens': True,
         'tracking_domain': None,
         'url_strip_qs': None}
        result = mandrill_client.messages.send(message=message, async=False, ip_pool='Main Pool')
        return result


    except mandrill.Error, e: 
        return 'A mandrill error occurred: %s - %s' % (e.__class__, e)


def sendReply(user, msg_id, msg, msg_raw, subject, recipient_name, notify):
    message                       = Message.get_by_id(int(msg_id))
    new_message                   = {}
    new_message['sender']         = user
    new_message['subject']        = subject
    new_message['sender_name']    = user.first_name + " " + user.last_name
    new_message['sender_email']   = user.alias
    new_message['receiver']       = message.sender
    new_message['receiver_name']  = recipient_name
    new_message['receiver_email'] = message.sender.email
    new_message['content']        = msg_raw
    new_message['type']           = 'reply_to'
    new_message['category']       = message.sender.user_profile
    new_message['date']           = strftime("%a, %d %b %Y %X +0000", gmtime())
    result                        = outBoundMail(new_message)
    msg                           = Message.create(new_message)
    new_notify                    = sendCopy(new_message, notify)
    user.notify_mail              = notify
    user.put()
    print new_notify
    print result
    return msg


def sendCopy(new_message, notify):
    from_email = new_message.get("sender_email")
    from_name  = new_message.get("sender_name")
    to_email   = notify
    to_name    = new_message.get("sender_name")
    subject    = "Notification"
    html       = mailContent.notification_sent
    reply_to   = "no-reply@mestglobalcommunity.appspotmail.com"
    tags       = "Outbound Mail"
    confirmation_url = "http://mestglobalcommunity.appspot.com/messages"
    variables  = [  {'name': 'username', 'content': new_message.get("sender_name")},
                    {'name': 'receiver_name', 'content': new_message.get("receiver_name")}, 
                    {'name': 'role', 'content'    : new_message.get("receiver").user_profile },
                    {'name':'read_url', 'content': confirmation_url}]
    merge      = False
    return sendOutboundMail(from_email, from_name, to_email, to_name, subject, html, tags, reply_to, variables, merge)


def composeNewMail(message):
    result                  = outBoundMail(message)
    user                    = message.get('sender')  
    notify                  = message.get('notification_email')
    msg                     = Message.create(message)
    user.notify_mail        = notify
    user.put()
    print user.notify_mail
    return result

def notifyEntrepreneur(message):
    user       = message.get("receiver")
    from_email = message.get("sender_email")
    from_name  = message.get("sender_name")
    to_email   = user.notify_mail
    to_name    = message.get("sender_name")
    subject    = "Notification"
    try:
        html   = mailContent.notification_received
    except:
        html   = "You just received a mail"
    reply_to   = "no-reply@mestglobalcommunity.appspotmail.com"
    tags       = "Outbound Mail"
    confirmation_url = "http://mestglobalcommunity.appspot.com/messages"
    variables  = [  {'name': 'username', 'content': message.get("receiver").first_name + " " +message.get("receiver").last_name},
                    {'name': 'sender_name', 'content': message.get("sender").first_name + " " +message.get("sender").last_name}, 
                    {'name': 'role', 'content'    : message.get("sender").user_profile },
                    {'name':'read_url', 'content': confirmation_url}]
    merge      = False
    return sendOutboundMail(from_email, from_name, to_email, to_name, subject, html, tags, reply_to, variables, merge)


def confirmUserMail(user):
    from_email = "no-reply@mestglobalcommunity.appspotmail.com"
    from_name  = "MEST Mentor Platform"
    to_email = user.notify_mail
    to_name  = user.first_name + " " + user.last_name
    subject = "Welcome to the MEST Mentor Platform!"
    confirmation_url = "http://mestglobalcommunity.appspot.com/signin"
    # confirmation_url = "http://localhost:8080/signin"
    
    if user.user_profile == "Mentor":
        html = mailContent.confirm_user_mentor
        variables = [{ 'name': 'username', 'content': to_name}]  

    elif user.user_profile == "Entrepreneur":
        html = mailContent.confirm_user
        variables = [{ 'name': 'username', 'content': to_name},
                    {'name': 'confirmation_url', 'content': confirmation_url}]

    reply_to = "<no-reply>@mestglobalcommunity.appspotmailmail.com"
    tags = "Confirmed User"
    merge = False
    return sendOutboundMail(from_email, from_name, to_email, to_name, subject, html, tags, reply_to, variables, merge)


def notificationMail(user):
    from_email = "no-reply@mestglobalcommunity.appspotmail.com"
    from_name  = "MEST Mentor Platform"
    to_email = user.notify_mail
    to_name  = user.first_name + " " + user.last_name
    user_profile = ""
    if user.user_profile == "Mentor":
        user_profile = "a Mentor"
    else:
        user_profile = "an Entrepreneur"        
    subject = "We've Received Your %s Application" %(user.user_profile)          
    html = mailContent.signup_template
    variables = [{ 'name': 'username', 'content': to_name},
                {'name': 'userprofile', 'content': user_profile}]
    reply_to = "<no-reply>@mestglobalcommunity.appspotmailmail.com"
    tags = "Confirmed User"
    merge = False
    return sendOutboundMail(from_email, from_name, to_email, to_name, subject, html, tags, reply_to, variables, merge)


    # if user.user_profile == "Mentor":
        # subject = "We've Received Your Mentor Application"    
    # elif user.user_profile == "Entrepreneur":
        # subject = "We've Received Your Entrepreneur Application"


# confirmation_url = "http://mestglobalcommunity.appspot.com/signin"
# confirmation_url = "http://localhost:8080/signin"
    # if user.user_profile == "Mentor":
    #     html = mailContent.signup_template
    #     variables = [{ 'name': 'username', 'content': to_name},
    #                 {'name': 'userprofile', 'content': user.user_profile}]  

    # elif user.user_profile == "Entrepreneur":
    #     html = mailContent.signup_template
    #     variables = [{ 'name': 'username', 'content': to_name},
    #                 {'name': 'confirmation_url', 'content': confirmation_url},
    #                 {'name': 'userprofile', 'content': user.user_profile}]
