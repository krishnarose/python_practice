# palindrome

def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    s_list = list(s)
    s_list.reverse()
    reverse_str = "".join(s_list)
    p = s == reverse_str
    print(p)
    print(type(p))
    print(s_list)
    print(reverse_str)
    return s == reverse_str

string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:    print("The string is not a palindrome.")