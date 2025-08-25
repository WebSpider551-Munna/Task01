text = input("Enter a String: ")
reversed_String = text[::-1]
if text == reversed_String:
    print(f'{text} is a Palindrome')
else:
    print(f'{text} is not a Palindrome')
    