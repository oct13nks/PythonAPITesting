import requests 
import json
import jsonpath 


def add_multiple_students():
    api_url="https://thetestingworldapi.com/Help/Api/studentsDetails"
    f=open("C:/Users/nitesh.singh/Desktop/api/add_new_student.son.txt")
    json_request=json.loads(f.read())
    response=requests.post(api_url,jsonrequest)

    print(response.status_code)
