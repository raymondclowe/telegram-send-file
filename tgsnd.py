# command line tool to send a file via telegram

# take two command line parameters, username and filename
# send the file to the user

# get the arguments from the command line

import sys
import os
from matplotlib.pyplot import text

import requests

from  users import users
from secrets import TG_TOKEN


  

# length of arguments must be in the range 2-3
if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("Usage: tgsnd.py <username> <filename>\n or \n Usage: tgsnd.py <username> read from stdin")
    sys.exit(1)

#first arguments is the username
username = sys.argv[1]

# if the username is not in the users dictionary then error and exit
if username not in users:
    print("Unknown user")
    sys.exit(1)

# second argument is the filename or absent and then this is stdin
if len(sys.argv) == 3:
    filename = sys.argv[2]
    # if filename doesn't exist
    if not os.path.isfile(filename):
        print("File not found")
        sys.exit(1)
    
    files = {'document': open(filename, 'rb')}


    url = 'https://api.telegram.org/bot{}/sendDocument?chat_id={}'.format(TG_TOKEN, users[username])
    r = requests.post(url=url, files= files)


    if r.status_code == 200:
        print("File sent")
    else:
        print("File not sent - error : {}".format(r.text))


else: # read from stdin
    text = sys.stdin.read()
    url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}'.format(TG_TOKEN, users[username])
    r = requests.post(url=url, data={'text': text})


    if r.status_code == 200:
        print("Text sent")
    else:
        print("Text not sent - error : {}".format(r.text))

