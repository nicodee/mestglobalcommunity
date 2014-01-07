import confirm_mentor_template

confirmation = "".join(['<!doctype html>','<html>','<head>','<title>MINC Community Signup Confirmation</title>','<meta name="viewport" content="width=device-width, initial-scale=1">',
    '<meta content="text/html; charset=UTF-8" http-equiv="Content-Type">','<link rel="stylesheet" href="https://app.divshot.com/themes/flat-ui/bootstrap.css">',
    '<link rel="stylesheet" href="https://app.divshot.com/css/bootstrap-responsive.css">','<link rel="stylesheet" href="https://app.divshot.com/themes/flat-ui/flat-ui.css">',
    '<link rel="stylesheet" href="https://djyhxgczejc94.cloudfront.net/builds/80037b02082b29f5f9cea127cab2a4ba4365ec67.css">','<script src="https://app.divshot.com/js/jquery.min.js"></script>',
    '<script src="https://app.divshot.com/js/bootstrap.min.js"></script>','</head>','<style type="text/css">','.container{','margin-top: 100px;','}','</style>','<body>',
    '<div class="container">','<div class="hero-unit hidden-phone">','<h1>Welcome to MINC *|user|*!</h1>','<p>Your MINC account has been created and you are ready to go! All you need',
    'to do now is click the link below to verify your email.</p>','<p></p>','<p></p>','<p>','<a class="btn btn-large btn-inverse" href="*|confirmationurl|*">Verify *|email|*</a>',
    '</p>','</div>','<a class="btn btn-large btn-primary btn-block visible-phone" href="http://mestglobalcommunity.appspot.com"><span class="btn-label">MINC Global Community</span></a>',
    '</div>','</body>','</html>'
])

confirm_user = confirm_mentor_template.entrepreneur_template

confirm_user_mentor = confirm_mentor_template.template

request = "".join(['<div style="background-color:#eeeeee;padding: 40px;border-radius:6px;color: rgb(52, 73, 94);">',
    '<h1 style="margin-top:-10px;">New Member Update</h1>','<p style="margin-bottom:40px;">',
    'Dear Admin, *|username|* just joined the Meltwater    Global Community as *|role|* and is awaiting your approval.',
    '</p><a href="*|confirmation_url|*">',
    '<button style="background-color: #34495e;color:#fff;border: none;font-size 16.5px;text-decoration: none;text-shadow: none;padding: 13px;border-radius:6px">',
    'Click here to confirm',
    '</button>',
    '</a></div>'])

notification_sent =  "".join(['<div style="background-color:#eeeeee;padding: 40px;border-radius:6px;color: rgb(52, 73, 94);">',
    '<h1 style="margin-top:-10px;">Meltwater Global Community</h1>','<h2 style="margin-bottom:40px;">',
    'Hello *|username|* , you just sent a mail to *|receiver_name|* (*|role|*).',
    '</h2><a href="*|read_url|*">',
    '<button style="background-color: #34495e;color:#fff;border: none;font-size 16.5px;text-decoration: none;text-shadow: none;padding: 13px;border-radius:6px">',
    'Click here to view the email',
    '</button>',
    '</a></div>'])

notification_received =  "".join(['<div style="background-color:#eeeeee;padding: 40px;border-radius:6px;color: rgb(52, 73, 94);">',
    '<h1 style="margin-top:-10px;">Meltwater Global Community</h1>','<h2 style="margin-bottom:40px;">',
    'Hello *|username|*, you just received a message from *|sender_name|* (*|role|*).',
    '</h2><a href="*|read_url|*">',
    '<button style="background-color: #34495e;color:#fff;border: none;font-size 16.5px;text-decoration: none;text-shadow: none;padding: 13px;border-radius:6px">',
    'Click here to view the email',
    '</button>',
    '</a></div>'])

signup_template = confirm_mentor_template.signup_template
# confirm_user = "".join(['<div style="background-color:#eeeeee;padding: 40px;border-radius:6px;color: rgb(52, 73, 94);">',
#     '<h1 style="margin-top:-10px;">Account confirmed</h1>','<p style="margin-bottom:40px;">',
#     'Dear *|username|*, your account on the MEST Global Community has been approved.',
#     '</p><a href="*|confirmation_url|*">',
#     '<button style="background-color: #34495e;color:#fff;border: none;font-size 16.5px;text-decoration: none;text-shadow: none;padding: 13px;border-radius:6px">',
#     'Click here to visit the site',
#     '</button>',
#     '</a></div>'])

# confirm_user_mentor = "".join(['<div style="background-color:#eeeeee;padding: 40px;border-radius:6px;color: rgb(52, 73, 94);">',
#     '<h1 style="margin-top:-10px;">Account confirmed</h1>','<p style="margin-bottom:40px;">',
#     'Dear *|username|*, your account on the MEST Global Community has been approved.'])