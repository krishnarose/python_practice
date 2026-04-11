list = [1, 2, 3, 4, 5]
print(list)
print(type(list))
list.append(6)
print(list)
list.insert(0, 0)
print(list)

list.reverse()
print(list)
list.sort()
print(list)
list.remove(3)
print(list)
print(list[0])
print(list[:1])
print(list[-1])

print("Length of list is: ", len(list))

sum = 0
for val in list:
    sum += val

average = sum / len(list)

print(f"the sum of {list} is {sum}")
print(f"the average of {list} is {average}")




