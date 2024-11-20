line = input()

def is_palindrome(string):
    s = string[::-1]
    if string == s:
        print("Yes")
    else:
        print("No")

is_palindrome(line)
        