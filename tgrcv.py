# command line tool to receive stuff via telegram


import sys
import os



import requests

from  users import users
import secrets


# set wait mode if the aguments contain "--wait" or "-w"
wait = False
if len(sys.argv) > 2:
    if sys.argv[2] == '--wait' or sys.argv[2] == '-w':
        wait = True  



TELEGRAM_API_URL = 'https://api.telegram.org/bot{}/'.format(secrets.TG_TOKEN)

r = requests.Session()

if wait:
    timeout = 60
else:
    timeout = 1
params = {'offset': 0, 'limit': 1, 'timeout': timeout}
response = r.get(TELEGRAM_API_URL + 'getUpdates', params=params)

response_json = response.json()

try:
    update_id = response_json['result'][0]['update_id']
    print(response_json['result'][0]['message']['text'])



    while len(response_json['result']) > 0:
        params = {'offset': update_id + 1, 'limit': 1, 'timeout': timeout}
        response = r.get(TELEGRAM_API_URL + 'getUpdates', params=params)
        response_json = response.json()
        if len(response_json['result']) > 0:
            update_id = response_json['result'][0]['update_id']
            print(response_json['result'][0]['message']['text'])

except:
    print("No message")

# clear anything in queue that wasn't processed 
params = {'offset': update_id + 1}
response = r.get(TELEGRAM_API_URL + 'getUpdates', params=params)