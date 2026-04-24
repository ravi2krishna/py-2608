# Student Management System

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
            print(students) # For confirmation we are printing dictionary
            
            
    
    elif choice == "2":
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
            
        print(students) # For confirmation we are printing dictionary
        
    elif choice == "3":
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
            
        print(students) # For confirmation we are printing dictionary
        
    elif choice == "4":
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
            total_score = 0 # 90 + 80 ....
            count_scores = 0
            
            for score in scores:
                total_score += score
                count_scores += 1
            
            avg_score = total_score / count_scores
            
            # Highest Score 
            high_score = scores[0] # 90
            
            for score in scores:
                if score > high_score:
                    high_score = score
                    
            # Lowest Score
            low_score = scores[0] # 90
            
            for score in scores:
                if score < low_score:
                    low_score = score
                    
            # Skill Count
            skill_count = 0 
            for skill in skills:
                skill_count += 1
                
        # Displaying Students Info 
        print(f"ID: {sid}")
        print(f"Name: {name}")
        print(f"All Scores: {scores}")
        print(f"Average Scores: {avg_score}")
        print(f"Highest Score: {high_score}")
        print(f"Lowest Score: {low_score}")
        print(f"All Skills: {skills}")
        print(f"Skills Count: {skill_count}")
        
    elif choice == "5":
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

