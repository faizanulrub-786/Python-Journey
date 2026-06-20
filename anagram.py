num1 = input("Enter the first string:- ")
num2 = input("Enter the second string:- ")
if sorted(num1.lower()) == sorted(num2.lower()):
    print("Both are Anagram")
else:
    print("Not an Anagram")