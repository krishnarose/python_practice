# Concept:Instance  & ClassAttributes.
# Create a class Player with :
# •a class variable player_count
# •instance variables name and level 
# Track how many players were created.

class Player:
    player_count = 0  # Class variable to track the number of players

    def __init__(self, name, level):
        self.name = name  # Instance variable for player's name
        self.level = level  # Instance variable for player's level
        Player.player_count += 1  # Increment player count when a new player is created

# Create instances of Player
player1 = Player("Alice", 1)
player2 = Player("Bob", 2)
player3 = Player("Charlie", 3)

# Display player information and total count
print("Player 1:")
print("Name:", player1.name)
print("Level:", player1.level)
print()

print("Player 2:")
print("Name:", player2.name)
print("Level:", player2.level)
print()

print("Player 3:")
print("Name:", player3.name)
print("Level:", player3.level)
print()

print("Total players created:", Player.player_count)