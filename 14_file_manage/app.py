# Student Management System -> Using Functional Style -> Using Persistent Storage

# Menu Based System -> In Future once you learn full stack, replace wth UI Elements like Buttons 

# System Setup -> READ ONLY (Tuple)

# System_info = ("Edify Technologies","Student Management System","v1") # Not recommended 
SYSTEM_INFO = ("Edify Technologies","Student Management System","v1") # recommended

# Admin Info 
ADMIN_INFO = ("9900990099","admin@edify.com")

# Display System Info On Start Up 
print("=" * 50)
print(f"Welcome To {SYSTEM_INFO[0]}")
print(f"Software Name {SYSTEM_INFO[1]} - {SYSTEM_INFO[2]}")
print("=" * 50)

# Core Functionality (CRUD)
# Adding Student -> id, name, scores, skills
# Representing Students Data Inside - Dictionary 
# https://jsoneditoronline.org/images/news/smart_json_formatting.png

# Import Utilities Required
import json 
import os 

# File To Store Students Data
FILE_NAME = "14_file_manage/students.json"

# Load Students Data From JSON File 
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,"r") as file_data:
            return json.load(file_data)
    else:
        return {}

# Save Students Data To JSON File 
def save_students():
    # TypeError: Object of type set is not JSON serializable
    # Fix Above Issue
    json_data_fix = {
        # {'101': {'name': 'Ravi', 'scores': [90], 'skills': {'python'}}}
        sid: {
            "name": data['name'],
            "scores": data['scores'],
            "skills": list(data['skills'])
        }
        for sid, data in students.items()
    }
    
    
    with open(FILE_NAME,"w") as file_data:
        json.dump(json_data_fix,file_data,indent=4)

# Students data inside Dictionary
students = load_students()

# Adding Student Function
def add_student():
        # Add Student
        print("=" * 30)
        print("Adding Student")
        print("=" * 30)
        student_id = input("Enter ID: ")
        if student_id in students:
            print("OOPS!! Student Already Exists")
        else:
            name = input("Enter Name: ").title()
            scores = []
            while True:
                score_input = input("Enter Score or type done: ")
                if score_input == "done":
                    break 
                if score_input.isdigit():
                    score_input = int(score_input)
                    if 0 <= score_input <= 100:
                        scores.append(score_input)
                    else:
                        print("Invalid Score, Scores should be (0-100)")
                else:
                    print("Invalid Score, Only Digits Allowed")
                    
            skills = set()
            while True:
                skill_input = input("Enter Skill or type done: ")
                if skill_input == "done":
                    break
                else:
                    skills.add(skill_input)
            
            print("========== Student Added ==========")
            students[student_id] = {
                "name": name,
                "scores": scores,
                "skills": skills
            }
            save_students() # Write Data To JSON File
            print(students) # For confirmation we are printing dictionary

# Updating Student Function
def update_student():
# Update Student
        print("=" * 30)
        print("Updating Student")
        print("=" * 30)
        
        student_id = input("Enter ID: ")
        if student_id in students:
            new_name = input("Enter New Name: ")
            students[student_id]['name'] = new_name
            print("=" * 30)
            print("Student Updated")
            print("=" * 30)
        else:
            print("OOPS!! Student ID Doesn't Exist")
        
        save_students() # Write Data To JSON File
        print(students) # For confirmation we are printing dictionary


# Deleting Student Function
def delete_student():
    # Delete Student
        print("=" * 30)
        print("Deleting Student")
        print("=" * 30)
        
        student_id = input("Enter ID: ")
        if student_id in students:
            students.pop(student_id)
            print("=" * 30)
            print("Student Deleted")
            print("=" * 30)
        else:
            print("OOPS!! Student ID Doesn't Exist")
        
        save_students() # Write Data To JSON File   
        print(students) # For confirmation we are printing dictionary


# Listing Students Function
def list_students():    
# List Students
        print("=" * 30)
        print("Reading Students")
        print("=" * 30)
        # {'101': {'name': 'Ravi', 'scores': [90], 'skills': {'python'}}}
        for sid,data in students.items():
            # sid = 101
            # data = {'name': 'Ravi', 'scores': [90], 'skills': {'python'}}
            name = data['name']
            scores = data['scores']
            skills = data['skills']

            # Average Score 
            avg_score = sum(scores) / len(scores)
            
            # Highest Score 
            high_score = max(scores)
                    
            # Lowest Score
            low_score = min(scores)
            
            # Skill Count
            skill_count = len(skills)
            
        # Displaying Students Info 
        print(f"ID: {sid}")
        print(f"Name: {name}")
        print(f"All Scores: {scores}")
        print(f"Average Scores: {avg_score}")
        print(f"Highest Score: {high_score}")
        print(f"Lowest Score: {low_score}")
        print(f"All Skills: {skills}")
        print(f"Skills Count: {skill_count}")

# Search Students Function
def search_students_Skill():    
# List Students
        print("=" * 30)
        print("Searching Students")
        print("=" * 30)
        skill_to_search = input("Enter Skill To Search: ")
        filtered_students = list(filter((lambda sid: skill_to_search in students[sid]['skills'] ), students))
        print(filtered_students)
        
        if filtered_students:
            print("=" * 30)
            print(f"Students With Skills {skill_to_search}")
            print("=" * 30)
            for sid in filtered_students:
                print(f"ID: {sid} - Name {students[sid]['name']}")
        else:
            print("=" * 30)
            print(f"No Students Found With Skills {skill_to_search}")
            print("=" * 30)
            

# Build Menu System For Different(CRUD) Operations 
while True:
    print("Choose An Option: ")
    print("1 - Add Student")
    print("2 - Update Student")
    print("3 - Delete Student")
    print("4 - List Students")
    print("5 - Search Student By Skill")
    print("6 - Exit Application")
    
    choice = input("Enter Your Choice (1-6): ")
    
    if choice == "1":
        add_student()
    
    elif choice == "2":
        update_student()
        
    elif choice == "3":
        delete_student()
        
    elif choice == "4":
        list_students()
        
    elif choice == "5":
        search_students_Skill()
        
    elif choice == "6":
        # Exit Application 
        print("=" * 30)
        print("Exiting Application")
        print("=" * 30)
        # Display System Info On Start Up 
        print("=" * 50)
        print(f"Admin Phone Number: {ADMIN_INFO[0]}")
        print(f"Admin Email ID: {ADMIN_INFO[1]}")
        print("=" * 50)
        break
    else:
        print("=" * 30)
        print("Invalid Option, Only use (1-5)")
        print("=" * 30)

