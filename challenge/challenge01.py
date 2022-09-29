#!/usr/bin/env python3

wordbank= ["indentation", "spaces"]
tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

print(wordbank)
wordbank.append(4)

print(wordbank)


num = input('Please the provide a number between 0 and 18: ')
student_name = tlgstudents[int(num)]
print(student_name)


print(f"{student_name} always uses {wordbank[len(wordbank)-1]} {wordbank[1]} to indent")
