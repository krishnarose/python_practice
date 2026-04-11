# Input two lists of integers from the user. Merge them into one list and sort the merged list.
# print("list1: ", list1)
# print("list2: ", list2)
# print(type(list1))
# print(type(list2))

list1 = input("Enter the first list of integers (comma-separated): ").split(",")
list2 = input("Enter the second list of integers (comma-separated): ").split(",")

# convert to int
list1 = [int(x.strip()) for x in list1]
list2 = [int(x.strip()) for x in list2]

# long process
# new_list = []

# for x in list1:
#     x = x.strip()     # space hatao
#     x = int(x)        # number me convert karo
#     new_list.append(x)

# list1 = new_list

marged_list = list1 + list2
print(f"Merged list: {marged_list}")

# sort the merged list
sorted_list = sorted(marged_list)
print(f"Sorted merged list: {sorted_list}")


# list1 = input("Enter first list: ").split(",")

# new_list1 = []
# for x in list1:
#     x = x.strip()
#     if x.isdigit():
#         new_list1.append(int(x))
#     else:
#         new_list1.append(x)

# print(new_list1)
