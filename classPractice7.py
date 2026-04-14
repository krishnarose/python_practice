
# concept : Constructor Overloading (with Default Parameters)
# Create  a class Person that allows the constructor to work with

# name only
# name + age
# name +age + address

# As direct constructor overloading (multiple constructors)are not allowed but we have to use default parameters to simulate constructor overloading 


class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print("Name:", self.name)
        
        if self.age is not None:
            print("Age:", self.age)
        
        if self.address is not None:
            print("Address:", self.address)

# Create instances of Person with different constructor parameters
person1 = Person("Alice")
person2 = Person("Bob", 30)
person3 = Person("Charlie", 25, "123 Main St")
# Display information for each person
print("Person 1:")
person1.display()
print("\nPerson 2:")
person2.display()
print("\nPerson 3:")
person3.display()
