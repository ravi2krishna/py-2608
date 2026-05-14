# OOP - Object Oriented Programming 

# class - Blue Print 
class Student:
    
    # Student Has Something - Characteristics / Properties / VARIABLES / Attributes
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # Student Does Something - Behaviors / Actions / METHODS 
    def student_studies():
        print("Student Is Studying Python")
        
    # Statements 
    print("Student Information System")
    print("Student Name: "+student_name)
    print("Student Email: "+student_email)
    
# Object - real entity 
student_object = Student()
# student_object.student_studies() # TypeError: Student.student_studies() takes 0 positional arguments but 1 was given

print("=" * 50)

# class - Blue Print 
class Student:
    
    # Student Has Something - Characteristics / Properties / VARIABLES / Attributes
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # Student Does Something - Behaviors / Actions / METHODS 
    # Added self which is object reference
    def student_studies(self):
        print("Student Is Studying Python")
        
    # Statements 
    print("Student Information System")
    print("Student Name: "+student_name)
    print("Student Email: "+student_email)
    
# Object - real entity 
student_object = Student()
student_object.student_studies()

print("=" * 50)

# class - Blue Print 
class Student:
    
    # Student Has Something - Characteristics / Properties / VARIABLES / Attributes
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # Student Does Something - Behaviors / Actions / METHODS 
    # Added self which is object reference
    def student_studies(self):
        print("Student Information System")
        print("Student Name: "+self.student_name) # recommended
        print("Student Email: "+student_object.student_email)
        print("Student Is Studying Python")
    
# Object - real entity 
student_object = Student()
student_object.student_studies()

print("=" * 50)

# class - Blue Print 
class Student:
    
    # Student Has Something - Characteristics / Properties / VARIABLES / Attributes
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # Student Does Something - Behaviors / Actions / METHODS 
    # Added self which is object reference
    def student_studies(self):
        print("Student Information System")
        print("Student Name: "+self.student_name) # recommended
        print("Student Email: "+self.student_email)
        print("Student Is Studying Python")
    
# Object - real entity 
student_object = Student()
student_object.student_studies()

print("=" * 50)

# Working with multiple objects
# class - Blue Print 
class Student:
    
    # Student Has Something - Characteristics / Properties / VARIABLES / Attributes
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # Student Does Something - Behaviors / Actions / METHODS 
    # Added self which is object reference
    def student_studies(self):
        print("Student Information System")
        print("Student Name: "+self.student_name) # recommended
        print("Student Email: "+self.student_email)
        print("Student Is Studying Python")
    
# Object - real entity 
student_ravi = Student()
student_ravi.student_studies()

student_mike = Student()
student_mike.student_studies()

student_john = Student()
student_john.student_studies()

print("=" * 50)

# Working with multiple objects using Constructor
# class - Blue Print 
class Student:
    
    # Student Has Something - Characteristics / Properties / VARIABLES / Attributes
    # student_name = "Ravi"
    # student_email = "ravi2krishna@gmail.com"
    
    # Constructor initialize a newly created object's attributes 
    def __init__(self,student_name,student_email):
        self.student_name = student_name
        self.student_email = student_email
    
    # Student Does Something - Behaviors / Actions / METHODS 
    # Added self which is object reference
    def student_studies(self):
        print("Student Information System")
        print("Student Name: "+self.student_name) # recommended
        print("Student Email: "+self.student_email)
        print("Student Is Studying Python")
    
# Object - real entity 
# student_ravi = Student() # TypeError: Student.__init__() missing 2 required positional arguments: 'student_name' and 'student_email'
student_ravi = Student("ravi","ravi2krishna@gmail.com") 
student_ravi.student_studies()

student_mike = Student("mike","mike@gmail.com")
student_mike.student_studies()

student_john = Student("john","john@gmail.com")
student_john.student_studies()

print("=" * 50)

# Instance Members
# class - Blue Print 
class Student:
    
    # Student Has Something - Characteristics / Properties / VARIABLES / Attributes
    # student_name = "Ravi"
    # student_email = "ravi2krishna@gmail.com"
    
    # Constructor initialize a newly created object's attributes 
    def __init__(self,student_name,student_email):
        # Below are Instance Variables -> self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
    
    # Student Does Something - Behaviors / Actions / METHODS 
    # Added self which is object reference
    # Below is Instance Method 
    def student_studies(self):
        print("Student Information System")
        print("Student Name: "+self.student_name) # recommended
        print("Student Email: "+self.student_email)
        print("Student Is Studying Python")
    
# Object - real entity 
# student_ravi = Student() # TypeError: Student.__init__() missing 2 required positional arguments: 'student_name' and 'student_email'
student_ravi = Student("ravi","ravi2krishna@gmail.com") 
student_ravi.student_studies()

student_mike = Student("mike","mike@gmail.com")
student_mike.student_studies()

student_john = Student("john","john@gmail.com")
student_john.student_studies()


print("=" * 50)

# Class Members
# class - Blue Print 
class Student:
    
    # Class Variables - shared by all the objects
    institute_name = "Digital Edify"
    
    # Constructor initialize a newly created object's attributes 
    def __init__(self,student_name,student_email):
        # Below are Instance Variables -> self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
    
    # Student Does Something - Behaviors / Actions / METHODS 
    # Added self which is object reference
    # Below is Instance Method 
    def student_studies(self):
        print("Student Information System")
        print("Institute Name: "+Student.institute_name) # recommended
        print("Student Name: "+self.student_name) # recommended
        print("Student Email: "+self.student_email)
        print("Student Is Studying Python")
        print("Institute Name: "+self.institute_name) # not recommended
    
# Object - real entity 
# student_ravi = Student() # TypeError: Student.__init__() missing 2 required positional arguments: 'student_name' and 'student_email'
student_ravi = Student("ravi","ravi2krishna@gmail.com") 
student_ravi.student_studies()

student_mike = Student("mike","mike@gmail.com")
student_mike.student_studies()

student_john = Student("john","john@gmail.com")
student_john.student_studies()

print("=" * 50)

# Class Members
# class - Blue Print 
class Student:
    
    # Class Variables - shared by all the objects
    institute_name = "Digital Edify"
    
    # Constructor initialize a newly created object's attributes 
    def __init__(self,student_name,student_email):
        # Below are Instance Variables -> self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
    
    # Student Does Something - Behaviors / Actions / METHODS 
    # Added self which is object reference
    # Below is Instance Method 
    def student_studies(self):
        print("Student Information System")
        print("Institute Name: "+Student.institute_name) # recommended
        print("Student Name: "+self.student_name) # recommended
        print("Student Email: "+self.student_email)
        print("Student Is Studying Python")
        print("Institute Name: "+self.institute_name) # not recommended
        
    # Class Method
    @classmethod
    def change_institute_name(cls,new_name):
        cls.institute_name = new_name
        # print("Student Name: "+self.student_name) # Accessing instance data inside a class method gives error 
    
# Object - real entity 
# student_ravi = Student() # TypeError: Student.__init__() missing 2 required positional arguments: 'student_name' and 'student_email'
student_ravi = Student("ravi","ravi2krishna@gmail.com") 
student_ravi.student_studies()

student_mike = Student("mike","mike@gmail.com")
student_mike.student_studies()

student_john = Student("john","john@gmail.com")
student_john.student_studies()

# Class Method Call
Student.change_institute_name("New Institute")
student_ravi = Student("ravi","ravi2krishna@gmail.com") 
student_ravi.student_studies()

student_mike = Student("mike","mike@gmail.com")
student_mike.student_studies()

student_john = Student("john","john@gmail.com")
student_john.student_studies()

# Static Members i.e only static methods
# class - Blue Print 
class Student:
    
    # Class Variables - shared by all the objects
    institute_name = "Digital Edify"
    
    # Constructor initialize a newly created object's attributes 
    def __init__(self,student_name,student_email):
        # Below are Instance Variables -> self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
    
    # Student Does Something - Behaviors / Actions / METHODS 
    # Added self which is object reference
    # Below is Instance Method 
    def student_studies(self):
        print("Student Information System")
        print("Institute Name: "+Student.institute_name) # recommended
        print("Student Name: "+self.student_name) # recommended
        print("Student Email: "+self.student_email)
        print("Student Is Studying Python")
        print("Institute Name: "+self.institute_name) # not recommended
        
    # Class Method
    @classmethod
    def change_institute_name(cls,new_name):
        cls.institute_name = new_name
        # print("Student Name: "+self.student_name) # Accessing instance data inside a class method gives error 
        
    # Static Method 
    @staticmethod
    def something():
        return "I Do Something that doesn't associate with Classes and Objects"
    
    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email # T and T 
    
# Object - real entity 
# student_ravi = Student() # TypeError: Student.__init__() missing 2 required positional arguments: 'student_name' and 'student_email'
student_ravi = Student("ravi","ravi2krishna@gmail.com") 
student_ravi.student_studies()

student_mike = Student("mike","mike@gmail.com")
student_mike.student_studies()

student_john = Student("john","john@gmail.com")
student_john.student_studies()

# Class Method Call
Student.change_institute_name("New Institute")
student_ravi = Student("ravi","ravi2krishna@gmail.com") 
student_ravi.student_studies()

student_mike = Student("mike","mike@gmail.com")
student_mike.student_studies()

student_john = Student("john","john@gmail.com")
student_john.student_studies()

# Call Static Method
print(Student.something())
print(Student.validate_email("ravi"))
print(Student.validate_email("ravi@gmailcom"))
print(Student.validate_email("ravi@gmail.com"))