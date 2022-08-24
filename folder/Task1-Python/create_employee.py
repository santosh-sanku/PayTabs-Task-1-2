""" Here i have created a new employee by sending a payload 
using the POST method """

import requests

url = "https://reqres.in/api/users"
payload = {
    "name": "santosh",
    "job": " Automation tester"
}

x = requests.post(url , json = payload)

print(x.text)

assert x.status_code == 201
print("Employee created successfully")

