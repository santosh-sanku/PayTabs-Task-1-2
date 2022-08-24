
from urllib import response
import requests
import json
import pprint

class api_test():

    """ In this below method i have requested the GET method 
            to get the list of employee """

    def list_of_employess(self):
    
        response = requests.get("https://reqres.in/api/users?page=2")
    
        response_code = response.status_code
    
        assert response_code == 200
    
        print("Response code matched successfully")
    
        """ Printing the Response Body"""
    
        print(response.text)



    """ Here the below method will create a new employee by sending a payload 
            using the POST method """

    def create_employee(self):

        url = "https://reqres.in/api/users"
        payload = {
            "name": "santosh",
            "job": " Automation tester"
        }

        x = requests.post(url , json = payload)

        print(x.text)

        assert x.status_code == 201
        print("Employee created successfully")



    """ Here in the below method is used to search
     the employee based on his first_name """
    
    def check_employe(self):

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



    """ In the below method the job of an employee is updated 
            based on the employee id """

    def update_job(self):

        url = "https://reqres.in/api/users/"
        params = {"page":"2"}

        response = requests.get(url, params)

        if response.status_code == 200:
    
            response_info = json.loads(response.text)
    
            #pprint.pprint(response_info['data'])
    
            for info in response_info['data']:
        
                if info['id'] == 8:
                    
                    update_data = {"job": "tester"}
                    
                    pprint.pprint(info['id'])
                    
                    info.update(update_data)
                    #pprint.pprint(response_info['data'])
                    
                    pprint.pprint(info)
                    
                    print('Success')
        
        else:
            print("Error: {response.status_code}")


s = api_test()

s.list_of_employess()
s.create_employee()
s.check_employe()
s.update_job()

