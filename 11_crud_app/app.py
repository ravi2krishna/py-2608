# Student Management System

# Menu Based System -> In Future once you learn full stack, replace wth UI Elements like Buttons 

# System Setup -> READ ONLY (Tuple)

# System_info = ("Edify Technologies","Student Management System","v1") # Not recommended 
SYSTEM_INFO = ("Edify Technologies","Student Management System","v1") # recommended

# Display System Info On Start Up 
print("=" * 50)
print(f"Welcome To {SYSTEM_INFO[0]}")
print(f"Software Name {SYSTEM_INFO[1]} - {SYSTEM_INFO[2]}")
print("=" * 50)

# Core Functionality (CRUD)
# Adding Student -> id, name, scores, skills
# Representing Students Data Inside - Dictionary 
# https://jsoneditoronline.org/images/news/smart_json_formatting.png

# Students data inside Dictionary
students = {}

# Build Menu System For Different(CRUD) Operations 
while True:
    print("Choose An Option: ")
    print("1 - Add Student")
    print("2 - Update Student")
    print("3 - Delete Student")
    print("4 - List Students")
    print("5 - Exit Application")
    
    choice = input("Enter Your Choice (1-5): ")
    
    if choice == "1":
        # Add Student
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
            print(students) # For confirmation we are printing dictionary
            
            
    
    elif choice == "2":
        # Update Student
        print("# Update Student")
        
    elif choice == "3":
        # Delete Student
        print("# Delete Student")
        
    elif choice == "4":
        # List Students
        print("# List Student")
        
    elif choice == "5":
        # Exit Application 
        print("# Exit Application")
    
    else:
        # Invalid Choice 
        print("# Invalid")

