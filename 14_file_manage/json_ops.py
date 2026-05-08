# Working With JSON Data / Files 

student = {
    "id": "101",
    "name": "Ravi",
    "email": "ravi2krishna@gmail.com",
    "courses": ["python","django","reactjs"],
    "gpa": 9.5
}

print(type(student))
print(student)

# Write Data To JSON File 
import json
with open("14_file_manage/student.json","w") as file_data:
    json.dump(student,file_data)

# Write Data To JSON File with Indentation
with open("14_file_manage/student.json","w") as file_data:
    json.dump(student,file_data,indent=4)

print("=" * 50)
    
# Read Data From JSON File 
with open("14_file_manage/student.json","r") as file_data:
    data = json.load(file_data)
    print(data)
    print(type(data))

print("=" * 50)
    
# Requirement: Get Student Name & Number Of Courses he joined from student.json file
with open("14_file_manage/student.json","r") as file_data:
    data = json.load(file_data)
print("Student Name: ",data['name'])    
print("Courses: ",data['courses']) 
print("Total Courses Enrolled: ", len(data['courses'])) 

# Requirement: Check If Student Passed Or Not, based on GPA above 7 from student.json 
with open("14_file_manage/student.json","r") as file_data:
    data = json.load(file_data)

if data['gpa'] > 7:
    print(f"{data['name']} has Passed")
else:
    print(f"{data['name']} has Failed")

print("=" * 50)
    
# File Based -> dump() & load()
# Object Based -> dumps() & loads()

student = {
    "id": "101",
    "name": "Ravi",
    "email": "ravi2krishna@gmail.com",
    "courses": ["python","django","reactjs"],
    "gpa": 9.5
}
print(type(student))

json_data = json.dumps(student) # Serialize obj to a JSON formatted str
print(type(json_data))
print(json_data)

string_data = '{"id": "101", "name": "Ravi", "email": "ravi2krishna@gmail.com", "courses": ["python", "django", "reactjs"], "gpa": 9.5}'
print(type(string_data))
dict_data = json.loads(string_data)
print(type(dict_data))
print(dict_data)

# Assume i'm a full stack developer 
# Requirement: We have an API, when requested we are getting JSON Data 
# https://dummyjson.com/

import requests
url = 'https://dummyjson.com/users'
response = requests.get(url)
print("HTTP Status Code: ",response.status_code)
print(response)
print(type(response))
print(response.text)
print(type(response.text))

data_fetched = response.text
api_data = json.loads(data_fetched)
print(type(api_data))

# Requirements: Find Number Of Users in the platform 
all_users = api_data['users']
print(all_users)
print("Number Of Users in platform: ",len(all_users))

# Requirements: Fetch all the usernames Of Users in the platform 
for user in all_users:
    print(user['id'], user['username'])
    

# Requirements: Fetch all the usernames Of Young Users in the platform i.e aged below 30
print("=" * 50)
print("         Young Users In Platform")
print("=" * 50)
for user in all_users:
    if user['age'] < 30:
        print(user['id'], user['username'])
        