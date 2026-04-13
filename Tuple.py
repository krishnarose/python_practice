# Tuple practice

tuple = (1,2,3,4,4,1,5)
print(tuple)
print(type(tuple))

#creating a emplty tuple

empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))

# creating a tuple with one element
single_element_tuple = (1,)
print(single_element_tuple)
print(type(single_element_tuple))


# accessing elements of A tuple using for loop

for val in tuple:
    print(val)

# accessing elements of a tuple using index

print(tuple[0])

# slicing a tuple
print(tuple[1:4])
print(tuple[:])

#tuple is immutable
#tuple[0] = 10  # this will give an error because we cannot change the value of a tuple

# write a program to seprate odd and even numbers from a tuple and store them in two different tuples
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
even_numbers = ()
odd_numbers = ()
for num in numbers:
    if num % 2 == 0:
        even_numbers += (num,)
    else:
        odd_numbers += (num,)
print("Even numbers: ", even_numbers)
print("Odd numbers: ", odd_numbers)

