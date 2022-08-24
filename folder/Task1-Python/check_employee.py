""" Here i have searched the employee based on his first_name """

import requests
import json
import pprint

url = "https://reqres.in/api/users"
params = {"page":"2"}

response = requests.get(url, params)

if response.status_code == 200:
    response_info = json.loads(response.text)
    pprint.pprint(response_info['data'])
    firstnamelist = []
    
    for firstname_info in response_info['data']:
       firstnamelist.append(firstname_info['first_name'])
    pprint.pprint(firstnamelist)
   
    if 'Tobias' in firstnamelist:
        pprint.pprint('Success')
    
    else:
       pprint.pprint('Fail')

else:
    pprint.pprint("Error: {response.status_code}")