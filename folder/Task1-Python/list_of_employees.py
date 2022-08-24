""" In this i have requested the GET method 
to get the list of employee """

from urllib import response
import requests

response = requests.get("https://reqres.in/api/users?page=2")

response_code = response.status_code
assert response_code == 200
print("Response code matched successfully")

""" Printing the Response Body"""
print(response.text)
