# a = 1.4
# b = 1

# print(type(a + b) )

# name = input("Enter your name: ")
# age = input("Enter Your Age:")

# print("Hello ",name,"! you are ",age," years old.")

# first_number = float(input("Enter first number: "))
# second_number = float(input("Enter second number"))

# sum = (first_number + second_number)
# differnce = (first_number - second_number)
# product = (first_number * second_number)
# quotient = (first_number % second_number)

# print("The sum of ",first_number," and ",second_number," is ",sum)
# print("The difference of ",first_number," and ",second_number," is ",differnce)
# print("The product of ",first_number," and ",second_number," is ",product)
# print("The quotient of ",first_number," and ",second_number," is ",quotient)

# a = int(input("Enter first number as integer: "))
# b = int(input("Enter second number as integer: "))
# c = float(input("enter third number as a float: "))

# ave = (a+b+c)/3
# print("avegarge of three number are: ", ave)

# number = input("enter a number: ")
# number2 = input("enter a number: ")
# sum = (float(number) + int(number2))
# print("sum", sum)
# print("Float value is:", float(number))
# print("Float value is:", int(number))

# x = 10 + 3 * 2 ** 2
# print(x)
# swap of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)

def sum(x, y):
    return x + y

result = sum(5, 10)
print("The sum is:", result)