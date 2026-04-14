# Concept:Inheritance
# Create a class Vehicle with attributes like brand and model. Create two subclasses Car and Bike that add extra attributes - seats (in Car) & engine_cc (in Bike)

class Vechicle:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
    

class Car(Vechicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

class Bike(Vechicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

# Create instances of Car and Bike
car1 = Car("Toyota", "Camry", 5)
bike1 = Bike("Honda", "CBR500R", 500)

# Display details of Car and Bike
print(f"Car Details: Brand: {car1.brand}, Model: {car1.model}, Seats: {car1.seats}")
print(f"Bike Details: Brand: {bike1.brand}, Model: {bike1.model}, Engine CC: {bike1.engine_cc}")

