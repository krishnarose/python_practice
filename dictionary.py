# Dictionary Practice
# A dictionary is a collection of key-value pairs. Each key is unique and maps to a value.

# creating a dictionary

my_dict = {
    "name" : "Jones",
    "age" : 30,
    "city" : "New York",
    "subjects" : ["Math", "Science", "English"],
    "is_student" : True,
}

# print(my_dict)
# print(type(my_dict))
# print(my_dict["subjects"]) #  if subjects key is not present in the dictionary it will give an error
# print(my_dict.get("age")) # if age key is not present in the dictionary it will return None
# print(my_dict.keys())   # it will return a list of all the keys in the dictionary
# print(my_dict.values()) # it will return a list of all the values in the dictionary
# print(my_dict.items()) # it will return a list of tuples where each tuple is a key-value pair in the dictionary

# add a new key-value pair to the dictionary
# my_dict["country"] = "USA"
# print(my_dict)

# # update the value of an existing key in the dictionary
# my_dict["age"] = 31
# print(my_dict)

# # add new marks 
# my_dict["marks"] = {"Math": 90, "Science": 85, "English": 88}
# print(my_dict)
# print(my_dict["marks"]["Math"]) # it will return the marks of Math subject

# creating a program to create a dictionary of students and their grades
# Writea menu-based program where user pressesa key(ʼAʼ,‘Bʼ,‘Cʼ,‘Dʼ,‘Eʼ)depending on the operation they want to perform on the dictionary
# 1. A. Add a student
# 2. B. Update a Grades
# 3. C. Search for a students
# 4. D. Display all students and their grades

# Dictionary to store students and grades
# students = {}

# while True:
#     print("\n===== MENU =====")
#     print("A. Add Student")
#     print("B. Update Grade")
#     print("C. Search Student")
#     print("D. Display All Students")
#     print("E. Exit")

#     choice = input("Enter your choice: ").upper()

#     # A. Add Student
#     if choice == 'A':
#         name = input("Enter student name: ")
#         grade = input("Enter grade: ")
#         students[name] = grade
#         print(f"{name} added successfully!")

#     # B. Update Grade
#     elif choice == 'B':
#         name = input("Enter student name to update: ")
#         if name in students:
#             grade = input("Enter new grade: ")
#             students[name] = grade
#             print(f"{name}'s grade updated!")
#         else:
#             print("Student not found!")

#     # C. Search Student
#     elif choice == 'C':
#         name = input("Enter student name to search: ")
#         if name in students:
#             print(f"{name}'s grade is {students[name]}")
#         else:
#             print("Student not found!")

#     # D. Display All Students
#     elif choice == 'D':
#         if students:
#             print("\nStudent List:")
#             for name, grade in students.items():
#                 print(f"{name} : {grade}")
#         else:
#             print("No students found!")

#     # E. Exit
#     elif choice == 'E':
#         print("Exiting program...")
#         break

#     else:
#         print("Invalid choice! Try again.")


students = {}

while True:
    print("\n===== MENU =====")
    print("1. Add Student")
    print("2. Add Subject & Marks")
    print("3. Delete Student")
    print("4. Delete Subject")
    print("5. Search Student")
    print("6. Display All")
    print("7. Exit")

    choice = input("Enter choice: ")

    # 1. Add Student
    if choice == '1':
        name = input("Enter student name: ")
        if name not in students:
            students[name] = {}
            print(f"{name} added!")
        else:
            print("Student already exists!")

    # 2. Add Subject & Marks
    elif choice == '2':
        name = input("Enter student name: ")
        if name in students:
            subject = input("Enter subject: ")
            marks = float(input("Enter marks: "))
            students[name][subject] = marks
            print("Subject added!")
        else:
            print("Student not found!")

    # 3. Delete Student
    elif choice == '3':
        name = input("Enter student name to delete: ")
        if name in students:
            del students[name]
            print("Student deleted!")
        else:
            print("Student not found!")

    # 4. Delete Subject
    elif choice == '4':
        name = input("Enter student name: ")
        if name in students:
            subject = input("Enter subject to delete: ")
            if subject in students[name]:
                del students[name][subject]
                print("Subject deleted!")
            else:
                print("Subject not found!")
        else:
            print("Student not found!")

    # 5. Search Student
    elif choice == '5':
        name = input("Enter student name: ")
        if name in students:
            print(f"{name}'s subjects and marks:")
            for sub, marks in students[name].items():
                print(f"{sub} : {marks}")
        else:
            print("Student not found!")

    # 6. Display All
    elif choice == '6':
        if students:
            for name, subjects in students.items():
                print(f"\n{name}:")
                for sub, marks in subjects.items():
                    print(f"  {sub} : {marks}")
        else:
            print("No data available!")

    # 7. Exit
    elif choice == '7':
        print("Exiting...")
        break

    else:
        print("Invalid choice!")

