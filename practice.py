# Given a list of words
#words = ["apple", "banana", "cherry", "date", "elderberry"] 
# Create a dictionary that maps each word to its length
#word_lengths = {word: len(word) for word in words}

words = ["apple", "banana", "cherry", "date", "elderberry"]

word_lengths ={}

# print(type(word_lengths))
# print(type(words))
# print(word_lengths)
# for word in words:
#     # print(word)
#     print(f"Length of  {word} is {len(word)}")
#     word_lengths[word] = len(word)

# print(word_lengths)


# Write a program that takes a string from the user and prints the number of spaces in the string.

string = input("Enter a string: ")
space_count = string.count(" ")
print(f"The number of spaces in the string is: {space_count}")
print("the total number of characters in the string is: ", len(string))

# removed space
no_space = string.replace(" ", "")
print("After removing spaces:", no_space)

#method 2
result = ""

for ch in string:
    if ch != " ":
        result += ch

print("After removing spaces through iteration:", result)

#method 3
no_space = "".join(string.split())
print("After removing spaces through split and join:", no_space)