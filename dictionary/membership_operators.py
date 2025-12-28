# Membership operators = used to test whether a value or variable is found a squence
#                        (sting,list,tuple,set or dictionary)
#                         1. in
#                         2. not in

# students = {"Minh","Quan","Trung"}
# student = input("Enter the name of a student: ") 
# if student in students:
#     print(f"{student} is a student")
# else:
#     print(f"{student} is not a student")


grades = {"Minh": "A","Quan":"B","Trung":"C"}
student = input("Enter the name of a student: ")
if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")

# email ="doanquangminh@gamil.com"
# if "@" in email and "." in email:
#     print("Valid email")
# else:
#     print("Invaild email")