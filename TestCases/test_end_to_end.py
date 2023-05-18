import requests
import json 
import jsonpath 


def test_add_student_data():
    API_URL="https://thetestingworldapi.com/api/studentsDetails"
    f=open("C:/Users/nitesh.singh/Desktop/api/Requestjson.json",'r')
    json_request=json.loads(f.read())
    response = requests.post(API_URL,json_request)
    print(response.text)

    id=jsonpath.jsonpath(response.json(),'id')

    print(id[0])


    # to add tech details 
    tech_api_url="https://thetestingworldapi.com/api/technicalskills"
    f=open("C:/Users/nitesh.singh/Desktop/api/Techdetails.json",'r')
    json_request=json.loads(f.read())
    response = requests.post(tech_api_url,json_request)
    print(response.text)
    

    #to add address details 

    address_api_url="https://thetestingworldapi.com/api/addresses"
    f=open("C:/Users/nitesh.singh/Desktop/api/address.json",'r')
    json_request=json.loads(f.read())
    response = requests.post(address_api_url,json_request)
    print(response.text)



    final_details="https://thetestingworldapi.com/api/FinalStudentDetails/7478748"
    response=requests.get(final_details)
    print(response.text)