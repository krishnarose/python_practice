import json
cities = {
    "Delhi": 4500000,
    "Mumbai": 5000000,
    "Bangalore": 3000000,
    "Chennai": 2000000

}

with open("cities.json", "w") as f:
    json.dump(cities, f, indent=4)

print("Cities data has been written to cities.json")

with open("cities.json", "r") as f:
    data = json.load(f)

print("City Populations:")
for city, population in data.items():
    print(f"{city} : {population}")

# Step 4: Ask user for new city and population
new_city = input("\nEnter new city name: ")
new_population = int(input("Enter population: "))

# Step 5: Update dictionary
data[new_city] = new_population

# Step 6: Save updated data back to JSON
with open("cities.json", "w") as file:
    json.dump(data, file, indent=4)

print("\nUpdated data saved successfully!")