# Working With CSV Files 

import csv

# Reading Data From CSV File
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        print(row)

print("=" * 50)

# Assume We Have 10K -> 100k Students Records In CSV File 
# Customer Requirement: Fetch me all the students from Hyderabad 
# Observation to be made: What format the data is in ?? List 
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
    # [name,email,mobile,address]
        # print(row[-1]) # by address
        if row[-1] == "Hyderabad":
            print(row)
            
print("=" * 50)

# Assume We Have 10K -> 100k Students Records In CSV File 
# Customer Requirement: Fetch me all the students from tcs  
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        # print(row[1]) # by email
        if row[1].endswith("@tcs.com"):
            print(row)
            
# NOW DATA SETS ARE CHANGED
# Assume We Have 10K -> 100k Students Records In CSV File 
# Customer Requirement: Fetch me all the students from Hyderabad 
# Observation to be made: What format the data is in ?? List 
with open("14_file_manage/sample.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
    # [name,email,mobile,address]
        # print(row[-1]) # by address
        if row[-1] == "Hyderabad":
            print(row)
            
print("=" * 50)

# Using DictReader for -> CHANGING DATA SETS 
# Assume We Have 10K -> 100k Students Records In CSV File 
# Customer Requirement: Fetch me all the students from Hyderabad 
# Observation to be made: What format the data is in ?? List 
with open("14_file_manage/sample.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        print(row) # data is in key value pairs
        # {'name': 'Hari', 'mobile': '9889032187', 'address': 'Jaipur', 'email': 'hari193@outlook.com'}
    
print("=" * 50)

# Using DictReader for -> CHANGING DATA SETS 
# Assume We Have 10K -> 100k Students Records In CSV File 
# Customer Requirement: Fetch me all the students from Hyderabad 
# Observation to be made: What format the data is in ?? List 
with open("14_file_manage/sample.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        # print(row) # data is in key value pairs
        # {'name': 'Hari', 'mobile': '9889032187', 'address': 'Jaipur', 'email': 'hari193@outlook.com'}
        if row['address'] == "Hyderabad":
            print(row)
            
print("=" * 50)

# Using DictReader for -> CHANGING DATA SETS -> Checking for Dynamic Nature(students.csv)
# Assume We Have 10K -> 100k Students Records In CSV File 
# Customer Requirement: Fetch me all the students from Hyderabad 
# Observation to be made: What format the data is in ?? List 
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        # print(row) # data is in key value pairs
        # {'name': 'Hari', 'mobile': '9889032187', 'address': 'Jaipur', 'email': 'hari193@outlook.com'}
        if row['address'] == "Hyderabad":
            print(row)
            
print("=" * 50)

# Writing Data using writer
with open("14_file_manage/emp.csv","w") as file_data:
    csv_writer = csv.writer(file_data)
    csv_writer.writerow(['name', 'email', 'mobile', 'address'])
    csv_writer.writerows([
        ['Ravi', 'ravi186@tcs.com', '9876055200', 'Bangalore'],
        ['Ramu', 'ramu661@tcs.com', '9833214959', 'Bangalore'],
        ['Deepak', 'deepak641@tcs.com', '9369382025', 'Chennai']
    ])

# Writing Data using DictWriter
fieldnames = ['name', 'email', 'mobile', 'address']
with open("14_file_manage/emp.csv","w") as file_data:
    csv_writer = csv.DictWriter(file_data,fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerow({'name': 'Mahesh', 'email': 'mahesh381@outlook.com', 'mobile': '9969450859', 'address': 'Hyderabad'})
    csv_writer.writerows([
        {'name': 'Lokesh', 'email': 'lokesh489@gmail.com', 'mobile': '9879744557', 'address': 'Hyderabad'},
        {'name': 'Santosh', 'email': 'santosh579@outlook.com', 'mobile': '9718726887', 'address': 'Hyderabad'},
        {'name': 'Naveen', 'email': 'naveen409@tcs.com', 'mobile': '9806720153', 'address': 'Hyderabad'}
    ])