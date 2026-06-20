number = input("Write the number:- ")
digit_spelling = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    }
output = ""
for ch in  number:
    output +=  digit_spelling.get(ch, "!") + " "

print(output)