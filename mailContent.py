import confirm_mentor_template


confirm_user = confirm_mentor_template.entrepreneur_template

confirm_user_mentor = confirm_mentor_template.template

request = "".join(['<div style="background-color:#eeeeee;padding: 40px;border-radius:6px;color: rgb(52, 73, 94);">',
    '<h1 style="margin-top:-10px;">New Member Update</h1>','<p style="margin-bottom:40px;">',
    'Dear Admin, *|username|* just joined the MEST Mentor Platform as *|role|* and is awaiting your approval.',
    '</p><a href="*|confirmation_url|*">',
    '<button style="background-color: #34495e;color:#fff;border: none;font-size 16.5px;text-decoration: none;text-shadow: none;padding: 13px;border-radius:6px">',
    'Click here to confirm',
    '</button>',
    '</a></div>'])

notification_sent =  "".join(['<div style="background-color:#eeeeee;padding: 40px;border-radius:6px;color: rgb(52, 73, 94);">',
    '<h1 style="margin-top:-10px;">MEST Mentor Platform</h1>','<h2 style="margin-bottom:40px;">',
    'Hello *|username|* , you just sent a mail to *|receiver_name|* (*|role|*).',
    '</h2><a href="*|read_url|*">',
    '<button style="background-color: #34495e;color:#fff;border: none;font-size 16.5px;text-decoration: none;text-shadow: none;padding: 13px;border-radius:6px">',
    'Click here to view the email',
    '</button>',
    '</a></div>'])

notification_received =  "".join(['<div style="background-color:#eeeeee;padding: 40px;border-radius:6px;color: rgb(52, 73, 94);">',
    '<h1 style="margin-top:-10px;">MEST Mentor Platform</h1>','<h2 style="margin-bottom:40px;">',
    'Hello *|username|*, you just received a message from *|sender_name|* (*|role|*).',
    '</h2><a href="*|read_url|*">',
    '<button style="background-color: #34495e;color:#fff;border: none;font-size 16.5px;text-decoration: none;text-shadow: none;padding: 13px;border-radius:6px">',
    'Click here to view the email',
    '</button>',
    '</a></div>'])

signup_template = confirm_mentor_template.signup_template