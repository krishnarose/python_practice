# Base class 1
class Herbivore:
    def eat_plants(self):
        print("Eats plants")

# Base class 2
class Carnivore:
    def eat_meat(self):
        print("Eats meat")

# Base class 3
class Omnivore:
    def eat_both(self):
        print("Eats both plants and meat")

# Child class inheriting from multiple classes
class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"I am a bear. My name is {self.name}")

# Create an instance of Bear
bear1 = Bear("Baloo")
# Display bear information and eating habits
bear1.display()
bear1.eat_plants()
bear1.eat_meat()
bear1.eat_both()