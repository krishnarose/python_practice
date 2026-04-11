# salary = int(input("Enter your salary: "))
# # salary = 30000


# if salary < 30000:
#     tax = salary * (5/100)
# elif (salary >= 30000 and salary < 70000):
#     tax = salary *(15/100)
# else: tax = salary * (25/100)

# print("Your tax is: ", tax)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# for i in range(a, b+1):
#     if(i % 2 == 0):
#         print(i, "is even")
#     # else:
#     #     print(i, "is odd")

def print_digits(n):
    while n > 0:
        digit = n % 10      # get last digit
        print(digit)
        n = n // 10         # remove last digit

number = int(input("Enter a number: "))
print_digits(number)

