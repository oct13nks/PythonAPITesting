import requests
import json
import jsonpath 



def test_add_student_data():
    API_URL="https://thetestingworldapi.com/api/studentsDetails"
    f=open("C:/Users/nitesh.singh/Desktop/api/Requestjson.json",'r')
    json_request=json.loads(f.read())
    response = requests.post(API_URL,json_request)
    print(response.text)


def test_get_student_data():
    API_URL="https://thetestingworldapi.com/api/studentsDetails/7478462"
    response = requests.get(API_URL)
    json_response=response.json()
    id=jsonpath .jsonpath(json_response,'data.id')
    assert id[0]== 7478462


def test_update_student_data():
    API_URL="https://thetestingworldapi.com/api/studentsDetails/7478462"
    f=open("C:/Users/nitesh.singh/Desktop/api/Requestjson.json",'r')
    json_request=json.loads(f.read())
    response = requests.put(API_URL,json_request)
    print(response.text)




def test_delete_student_data():
    API_URL="https://thetestingworldapi.com/api/studentsDetails/7478462"
    response = requests.delete(API_URL)
    json_response=response.json()
    print(json_response)
   

def test_get_student_data():
    API_URL="https://thetestingworldapi.com/api/studentsDetails/7478462"
    response = requests.get(API_URL)
    json_response=response.json()
    id=jsonpath .jsonpath(json_response,'data.id')
    print(json_response)
    assert id[0]== 7478462