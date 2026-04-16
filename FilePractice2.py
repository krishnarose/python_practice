# # word search in file in line no 
# with open("Sample.txt", "r") as file:
#     lines = file.readlines()

# word_to_search = input("Enter the word to search: ")
# found = False
# for i, line in enumerate(lines, start=1):
#     if word_to_search in line:
#         print(f"The word '{word_to_search}' is found in line {i}.")
#         found = True

# if not found:
#     print(f"The word '{word_to_search}' is not found in the file.")

# data = True
# line = 1
# word = "python"
# with open("Sample.txt", "r") as file:
#     while data:
#         data = file.readline()
#         if word in data:
#             print(f"The word '{word}' is found in line {line}.")
#         line += 1

# Write a program that tries to open "data.txt" a file in read mode. If the file does not exist, catch the exception and print "File not found!"

try:
    with open("data.txt", "r") as f:
        data = f.read()

except FileNotFoundError:
    print("File not found!")

else:
    print("File opened successfully!")
    print(data)

finally:
    print("Program execution completed.")