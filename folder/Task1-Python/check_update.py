from cgitb import text
import requests
import json

response = requests.get("https://reqres.in/api/users?page=2")

json_data = json.loads(response.text)

item = "santosh"

for i in json_data:
    if item.lower() == i['']






"""
for i in json_data:
    first_name = response.json()['data'][i]['first_name']
    assert first_name == "George"

response_code = response.status_code
assert response_code == 200
print("Response code matched successfully")
"""