#This file is part of emailvalid. The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.

'''
Checks a comma separated list of eMails
'''

__version__ = '1.0'

import re


def check_email(email):
    """ Get if email is valid. @ and . characters validation
    :email: str
    return: True or False
    """
    patern = re.compile(r'''^[A-Za-z0-9\.!#\$%&'\*\+-/=\?\^_`\{|\}~]+'''
            '''@[A-Za-z0-9\.!#\$%&'\*\+-/=\?\^_`\{|\}~]+\.[a-zA-Z]*$''')
    if not email:
        return False
    email = email.replace(';', ',')  # Replace emails separator ; -> ,
    emails = email.split(',')
    for email in emails:
        if not re.match(patern, email.strip()):
            return False
    return True