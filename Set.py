# # creating a set 
# my_set = {1,2,3,4,5,5,3,3,}
# print(my_set)
# print(type(my_set))

# # creating an empty set
# empty_set = set()
# print(empty_set)
# print(type(empty_set))

# # adding elements to a set
# my_set.add(6)
# print(my_set)

# # removing elements from a set
# my_set.remove(3)
# print(my_set)

# # checking if an element is in a set
# print(4 in my_set)

# # set operations 
# set1 = {1,2,3,4}
# set2 = {3,4,5,6}
# print("Union: ", set1 | set2)
# print("Intersection: ", set1 & set2)
# print("Difference: ", set1 - set2)
# print("Symmetric Difference: ", set1 ^ set2)

# # 
# print("Length of set is: ", len(my_set))
# print(f"union of {set1} and {set2} is: {set1.union(set2)}")
# print(f"intersection of {set1} and {set2} is: {set1.intersection(set2)}")

# Write a program to check whether two lists share no common elements

# list1 = [1,2,3,4]
# list2 = [5,6,7,8,4]
# set1 = set(list1)
# set2 = set(list2)
# print("Do the lists share no common elements?", set1.isdisjoint(set2))


# Given a list, print all elements that appear more than once in the list.
# list1 = [1, 2, 3, 4, 5, 2, 3]
# set1 = set()
# duplicates = set()

# for item in list1:
#     if item in set1:
#         duplicates.add(item)
#     else:
#         set1.add(item)

# print("Elements that appear more than once:", duplicates)


# Ask the user for a string and print
#  1.   All unique  characters
#  2.   The count of unique characters

string = input("Enter a string: ")
no_space = "".join(string.split())
unique_characters = set(no_space)
print("Unique characters: ", unique_characters)
print("Count of unique characters: ", len(unique_characters))