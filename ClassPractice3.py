# Create a class Student with private attributes _name, _roll_no, and _marks. Provide getter and setter methods with validation (e.g., marks cannot be negative, roll number has to be between 1 & 100, name cannot be empty)

class Student:
    def __init__(self, name, roll_no, marks):
        self.__name = None
        self.__roll_no = None
        self.__marks = None
        
        # Set the attributes using the setter methods to ensure validation
        self.set_name(name)
        self.set_roll_no(roll_no)   
        self.set_marks(marks)
    
    def set_name(self, name):
        if name.strip() == "":
            print("Name cannot be empty.")
        else:
            self.__name = name

    def get_name(self):
        return self.__name
    
    def set_roll_no(self, roll_no):
        if 1 <= roll_no <= 100:
            self.__roll_no = roll_no
        else:
            print("Roll number must be between 1 and 100.")
    def get_roll_no(self):
        return self.__roll_no
    def set_marks(self, marks):
        if marks < 0:
            print("Marks cannot be negative.")
        else:
            self.__marks = marks
    def get_marks(self):
        return self.__marks 
    

# Create an instance of Student
student1 = Student("John Doe", 25, 85)
# Display student information
print(f"Name: {student1.get_name()}")
print(f"Roll No: {student1.get_roll_no()}")
print(f"Marks: {student1.get_marks()}")
# Attempt to set invalid values
student1.set_name("")  # Invalid name
student1.set_roll_no(150)  # Invalid roll number
student1.set_marks(-10)  # Invalid marks
# Display student information again to see the effect of invalid inputs
print(f"Name: {student1.get_name()}")
print(f"Roll No: {student1.get_roll_no()}")
print(f"Marks: {student1.get_marks()}")

